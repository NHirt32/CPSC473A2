import file
import naiveBayes as nb

trainFile, testFile = file.input()

trainDF, testDF = file.read(trainFile, testFile)
predDF = nb.master(trainDF, testDF)
file.output(predDF)
