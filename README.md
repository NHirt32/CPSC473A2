# CPSC 473 A1

## Description:
This Python project's goal is to take in two seperate CSV files and make predictions on the 'Play' column of the test CSV file.

## Requirements
This project requires an installation of Python as well as Pandas.

## Usage:
Navigate to your local folder that contains the project files and run the following command:<br>
python main.py DATACSVFILENAME.csv SAMPLEINPUTFILENAME.csv 

## File Structure:
### main.py:
This file contains calls to all seperated functionality

### file.py:
This file contains user interactions such as terminal call parameter handling as well as reading and outputting files.

### naiveBayes.py:
This function handles our probability calculations. It has a master function that handles the overall Naive Bayes calculation as well as several helper functions that handle individual and conditional probability calculations.



