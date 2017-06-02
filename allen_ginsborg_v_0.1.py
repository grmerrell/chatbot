import pronouncing
import random
import sys
from nltk.corpus import wordnet as wn

#################################################################
# Common functions ##############################################
#################################################################

def rhymeSayer(content):
    """
		Takes user input and pulls off the last part of their line
		and replaces it with a random rhyming word then returns 
		what they said - the last word + a word that rhymes with the last word
	"""
    line = content.rsplit(' ', 1)[0]
    word_to_rhyme = content.rsplit(' ', 1)[-1]
    rhyme_list = pronouncing.rhymes(word_to_rhyme)
    rhyme = random.choice(rhyme_list)
    return line + ' ' + rhyme

def synonym(syn):
	line = syn.rsplit(' ', 1)[0]
	syn = syn.rsplit(' ', 1)[-1]

	print syn

	store = []
	for synset in wn.synsets(syn):
		for lemma in synset.lemmas():
			store.append(lemma)
	store

	elements = []

	for index, element in enumerate(store):
		elements.append(element.name())

    
	stored_elements = []

	for element in elements:
		if element != elements[0]:
			stored_elements.append(element)


	rand_thes = random.choice(stored_elements)
	return line + ' ' + rand_thes


#################################################################
# /Common functions #############################################
#################################################################

#################################################################
# Slack integration #############################################
#################################################################
if len(sys.argv)>1: # If command line arguments are provided, attempt to connect to Slack. Otherwise, proceed via CLI
    import time
    from slackclient import SlackClient # Don't forget to pip install this
    BOT_ID = sys.argv[1] # First argument is bot's User ID, like U0ABCDEF
    slack_client = SlackClient(sys.argv[2]) # Second argument is private key, like xoxb-1234567890-ABCDEFGHIJKLMNO
    AT_BOT = "<@" + BOT_ID + ">"

def handle_command(command, channel):
    """
		Receives commands directed at the bot and replies in rhyme.
	"""
    output_string = rhymeSayer(command)
    slack_client.api_call(
     "chat.postMessage",
     channel=channel,
     text=output_string,
     as_user=True)

def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and BOT_ID != output['user']:
                # return text after the @ mention, whitespace removed
                if AT_BOT in output['text']:
                    handle_command(output['text'].split(AT_BOT)[1].strip().lower(),output['channel'])
                else:
                    handle_command(output['text'].strip().lower(),output['channel'])
    return None, None

if __name__ == "__main__" and len(sys.argv) > 1:
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("Slack connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")

#################################################################
# /Slack integration ############################################
#################################################################

#################################################################
# Command line interface ########################################
#################################################################

# this is where the users input goes in
content = raw_input("""Allen ginsborg here ready to spit rhymes.  
	What mad lyric should I spit this time?>>>""")

content_with_rhymes = rhymeSayer(content)
print content_with_rhymes

# next, replace the end of a line with a synonym
# then, not and an antonym

print("Now we're going to have you enter a line and i'll replace the last \
	word with a similar word that's not the same"
                                              )

syn = raw_input("bro you want me to switch up your last word?>>>")

synonymized_words = synonym(syn)
print synonymized_words

#################################################################
# /Command line interface #######################################
#################################################################