import sys
import pandas as pd

def input():
    """
    This function analyzes user input from a terminal call and passes forward values to rest of program

    Returns:
        A tuple containing the file names of our test and input csv files (Relative path)
    """

    if len(sys.argv) != 3:
        print('Incorrect number of arguments (Should be 3)')
        sys.exit(1)

    trainFile = sys.argv[1]
    testFile = sys.argv[2]

    return trainFile, testFile

def read(trainFile, testFile):
    """
    This function reads in CSV files into pandas DataFrames

    Params:
        trainFile (String): A string containing the relative path of our training data CSV file
        testFile (String): A string containing the relative path of our training data CSV file
    Returns:
        A tuple containing our training and testing DataFrames
    """

    trainDF = pd.read_csv(trainFile)
    testDF = pd.read_csv(testFile)

    return trainDF, testDF

def output(predDF):
    """
    This function outputs our prediction DataFrame as a csv file

    Params:
        predDF (DataFrame): Our initial test DataFrame with our predictions appended to it

    """

    predDF.to_csv('PredictedResults.csv', index=False)
