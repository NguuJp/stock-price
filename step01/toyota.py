from pandas_datareader import data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import yfinance as yf

from package.module_company_stock import company_stock

# TOYOTAの株価を取得
company_code = '7203.JP'
start = dt.datetime(2020, 1, 1)
end = dt.datetime(2023, 4, 1)

company_stock(company_code, start, end)