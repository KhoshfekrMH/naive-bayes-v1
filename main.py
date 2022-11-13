import pandas as pd

dataSets = pd.read_excel('dataset.xlsx')

IQ = dataSets[1]
passAndFail = dataSets[2]


# region 1.average of each column (IQ and passAndFail)
def average(lst):
    return sum(lst) / len(lst)


averageIQ = average(IQ)
averagePassAndFail = average(passAndFail)
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
