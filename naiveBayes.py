from functools import reduce
import operator

targetState = "no"
predictionList = []

def prob(feature, colName, trainDF):
    """
    This function figures out the occurrence probability of individual features

    Params:
        target (String): The value we are trying to find the probability of
        trainDF (DataFrame):    The DataFrame we are searching for occurrences of the target
    Returns:
        Numeric value of probability of our target in the training DataFrame
    """
    featureCount = trainDF[colName].value_counts()[feature]
    featureProb = featureCount/len(trainDF)

    return featureProb

def conditionalProb(feature, colName, req, trainDF):
    """
    This function calculated the conditional probability of a feature given a requirement

    Params:
        target (String): The value we are trying to find the probability of
        trainDF (DataFrame):    The DataFrame we are searching for occurrences of the target
    Returns:
        The conditional probability of our feature given a requirement in our training DataFrame
    """

    reqRows = trainDF[colName].loc[trainDF['play'] == req]
    featureCount = reqRows.value_counts()[feature]
    overallReqRows = len(reqRows)
    targetProb = featureCount/overallReqRows

    return targetProb

def master(trainDF, testDF):
    """
    This function takes our two DataFrames and predicts our target "play" off the features of our training data

    Params:
        trainDF (DataFrame): DataFrame containing our training data
        testDF (DataFrame): DataFrame containig our testing data
    Returns:
        DataFrame of our test data with our appended predictions
    """

    featureProbList = []
    conditionalProbList = []

    # Increment through every row in our test DataFrame
    for index, row in testDF.iterrows():
        # Incrementing through each feature of row
        for colName, value in row.items():
            # Calculating probability of individual features
            featureProbList.append(prob(value, colName, trainDF))
            conditionalProbList.append(conditionalProb(value, colName, targetState, trainDF))

        reqProb = prob(targetState, 'play', trainDF)

        featureProbProduct = reduce(operator.mul, featureProbList)
        conditionalProbProduct = reduce(operator.mul, conditionalProbList)

        bayesProb = (conditionalProbProduct * reqProb) / (featureProbProduct)

        if (bayesProb > 0.5):
            predictionList.append('no')
        else:
            predictionList.append('yes')

    testDF['play'] = predictionList

    return testDF