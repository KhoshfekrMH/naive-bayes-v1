import pandas as pd

dataSets = pd.read_excel('dataset.xlsx')

IQ = dataSets[1]
passAndFail = dataSets[2]


def average(lst):
    return sum(lst) / len(lst)


averageIQ = average(IQ)
averagePassAndFail = average(passAndFail)

