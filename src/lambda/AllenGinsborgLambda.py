'''
This is a facebook bot to create poems by rhyming with user input.
'''

import boto3
import json
import logging
import os
import requests
import allen_ginsborg

from base64 import b64decode


ENCRYPTED_EXPECTED_TOKEN = os.environ['kmsEncryptedToken']
APP_TOKEN = os.environ['appToken']

kms = boto3.client('kms')
expected_token = kms.decrypt(CiphertextBlob=b64decode(ENCRYPTED_EXPECTED_TOKEN))['Plaintext']
decrypted_app_token = kms.decrypt(CiphertextBlob=b64decode(APP_TOKEN))['Plaintext']

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def respond(err, res=None, code='200'):
    return {
        'statusCode': code,
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def send_message(recipient, text):
    """Send the message text to recipient with id recipient.
    """
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
        params={"access_token": decrypted_app_token},
        data=json.dumps({
            "recipient": {"id": recipient},
            "message": {"text": text.decode('unicode_escape')}
        }),
        headers={'Content-type': 'application/json'})
    if r.status_code != requests.codes.ok:
        logger.error(r.text)


def lambda_handler(event, context):
    # Check for GET request from facebook to verify endpoint
    if ('hub.mode' in event and event['hub.mode'] == 'subscribe' ):
        queryparams = event['queryStringParameters']
        challenge = queryparams['hub.challenge']
        token = queryparams['hub.verify_token']
        if token != expected_token:
            logger.error("Request token (%s) does not match expected", token)
            return respond(Exception('Invalid request token'), None, '403')
        else:
            logger.info("Successful verification")
            return respond(None, int(challenge))
    # Process POST request
    else:
        data = json.loads(event['body'])
        if ('object' in data and data['object'] == 'page'):
            logger.info(data)
            for entry in data['entry']:
                for msg in entry['messaging']:
                    if 'message' in msg and 'text' in msg['message']:
                        # TODO: get new message here
                        send_message(msg['sender']['id'], msg['message']['text'])
        return respond(None, "Ok")
