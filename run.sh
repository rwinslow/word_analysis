#!/usr/bin/env bash

# Load dependencies
apt-get install python3

# Set permissions for program
chmod a+x ./src/word_analysis.py

# Run program with the input directory wc_input and output files wc_result and med_result in wc_output
python3 ./src/word_analysis.py ./wc_input ./wc_output/wc_result.txt ./wc_output/med_result.txt