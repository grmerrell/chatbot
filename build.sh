#!/bin/bash
####################################
#
# Build the necessary zip for lambda upload.
#
####################################
rm build/*
cd libs
zip -r ../build/lambdaBuild.zip ./*
zip -j ../build/lambdaBuild.zip ../src/lambda/*
cd ../src/nlp
zip -r ../../build/lambdaBuild.zip ./allen_ginsborg

echo "Zip built"
