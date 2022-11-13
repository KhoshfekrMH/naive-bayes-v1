import pandas as pd
import statistics
import math

dataSets = pd.read_excel('dataset.xlsx')

IQ = dataSets[1]
passAndFail = dataSets[2]

# region 1.average of each column (IQ and passAndFail)
Pass = []
Fail = []
for i in range(7):
    if passAndFail[i] == 1:
        Pass.append(passAndFail[i])
    else:
        Fail.append(passAndFail[i])

averagePass = len(Pass) / len(passAndFail)
averageFail = len(Fail) / len(passAndFail)

# endregion

# region 2.creation of IQ of passers and failures by passAndFail column
passers = []
failures = []

sumIQAndPassAndFail = IQ + passAndFail
for i in range(7):
    if passAndFail[i] == 1:
        targetIQ = sumIQAndPassAndFail[i] - passAndFail[i]
        passers.append(targetIQ)
    else:
        targetIQ = sumIQAndPassAndFail[i] - passAndFail[i]
        failures.append(targetIQ)

# endregion

# region 3.mean , std and variance

failedIQMean = statistics.mean(failures)
passedIQMean = statistics.mean(passers)

failedIQStd = statistics.stdev(failures)
passedIQStd = statistics.stdev(passers)

# failedIQVariance = statistics.variance(failures)
# passedIQVariance = statistics.variance(passers)

# endregion

# region final solution with NormPdf with xtest = 99 tested
xtest = int(input("Enter your IQ : "))  # write your IQ on terminal

failedIQNormPdf = (1 / math.sqrt(2) * failedIQStd) * math.exp(-1 / 2 * (xtest - failedIQMean) ** 2) * averageFail
passedIQNormPdf = (1 / math.sqrt(2) * passedIQStd) * math.exp(-1 / 2 * (xtest - passedIQMean) ** 2) * averagePass

if failedIQNormPdf > passedIQNormPdf:
    print('Navies Bayes prediction is "failed"')
else:
    print('Navies Bayes prediction is "passed"')
# endregion
