#!/bin/bash

# Clone the SemgrepAnalyzer repository
git clone https://github.com/m14r41/SemgrepAnalyzer.git ~/test/SemgrepAnalyzer

# Rename the script and make it executable
cd ~/test/SemgrepAnalyzer && mv semgrepAnalyzer.py semgrepAnalyzer && chmod +x semgrepAnalyzer

# Move the script to /usr/local/bin with sudo
sudo mv semgrepAnalyzer /usr/local/bin

# Navigate back to the test directory and delete the SemgrepAnalyzer folder
cd ~/test && rm -rf SemgrepAnalyzer
