#!/bin/bash
####################################
#
# Build the necessary lib files and zip for lambda upload.
#
####################################

# build libs
echo "Building library files..."
rm -rf ./libs/*
pip install requests -t ./libs/
pip install pronouncing -t ./libs/
pip install nltk -t ./libs/
pip install setuptools -t ./libs/
echo "Library files built."
# build source
echo "Building source zip..."
mkdir build
rm build/lambdaBuild.zip
cd libs
zip -r ../build/lambdaBuild.zip ./*
zip -j ../build/lambdaBuild.zip ../src/lambda/*
cd ../src/nlp
zip -r ../../build/lambdaBuild.zip ./allen_ginsborg
cd ../../
echo "Zip built"
