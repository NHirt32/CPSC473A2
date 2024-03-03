import file
import naiveBayes as nb

# trainFile, testFile = file.input()

trainDF, testDF = file.read('Data.csv', 'SampleInput.csv')
predDF = nb.master(trainDF, testDF)
file.output(predDF)
