predictionList = []

def prob(feature, trainDF):
    """
    This function figures out the occurrence probability of individual features

    Params:
        target (String): The value we are trying to find the probability of
        trainDF (DataFrame):    The DataFrame we are searching for occurrences of the target
    Returns:
        Numeric value of probability of our target in the training DataFrame
    """
    featureCount = trainDF.value_counts()[feature]
    featureProb = featureCount/len(trainDF)

    return featureProb

def conditionalProb(feature, req, trainDF):
    """
    This function

    Params:
        target (String): The value we are trying to find the probability of
        trainDF (DataFrame):    The DataFrame we are searching for occurrences of the target
    Returns:
        The conditional probability of our feature given a requirement in our training DataFrame
    """

    reqRows = trainDF.loc[trainDF['play'] == req]
    featureCount = reqRows.value_counts()[feature]
    overallReqRows = len(reqRows)
    targetProb = featureCount/overallReqRows

    return targetProb

def master(trainDF, testDF):
    """
    This function takes our two DataFrames and predicts our target "play" off the features of our training data

    Params:
        trainDF (DataFrame): DataFrame containing our training data
        testDF (DataFrame): DataFrame containg our testing data
    Returns:

    """

    featureProbList = []
    conditionalProbList = []

    # Increment through every row in our test DataFrame
    for row in testDF.iterrows():
        # Incrementing through each feature of row
        for value in row:
            # Calculating probability of individual features
            featureProbList.append(prob(value, trainDF))
            conditionalProbList.append(conditionalProb(value, "no", trainDF))

    reqProb = prob("no", trainDF)

    overallProb =



    return