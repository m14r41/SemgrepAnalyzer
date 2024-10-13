#!/bin/bash

# Clone the SemgrepAnalyzer repository
git clone https://github.com/m14r41/SemgrepAnalyzer.git

# Navigate into the cloned repository
cd SemgrepAnalyzer

# Rename the script and make it executable
mv semgrepAnalyzer.py semgrepAnalyzer
chmod +x semgrepAnalyzer

# Move the script to /usr/local/bin with sudo
sudo mv semgrepAnalyzer /usr/local/bin

# Go back to the parent directory and delete the SemgrepAnalyzer folder
cd .. && rm -rf SemgrepAnalyzer
