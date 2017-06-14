## Allen Ginsborg Project

A facebook bot designed to produce poems from user input. It is built to run in AWS lambda.

## Build

To build the necessary library dependencies and zip file for uploading to lambda, you must run the build.sh command from the chatbot directory.

If successful, the zip will be located in the build directory as 'lambdaBuild.zip'.

## Deployment

Upload the zip to lambda and set the two necessary environment variables.
* kmsEncryptedToken (key for kms encryption/decryption)
* appToken (the token given to facebook for verification)

The tokens should be encrypted using the aws helper. More info: http://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html
