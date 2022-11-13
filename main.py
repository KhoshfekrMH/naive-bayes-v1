import pandas as pd
from openpyxl import Workbook

dataSets = pd.read_excel('dataset.xlsx')

IQ = dataSets[1]
passAndFail = dataSets[2]
