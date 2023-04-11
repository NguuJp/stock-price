from pandas_datareader import data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import yfinance as yf


def company_stock(company_code, start, end):

    df = data.DataReader(company_code, 'stooq') # stooqからデータを取得
    df = df[(df.index >= start) & (df.index <= end)] # 期間指定

    date = df.index # X軸に日付を指定
    price = df['Close'] # Y軸に株価を指定

    # 移動平均線の計算
    span01 = 5
    span02 = 25
    span03 = 50

    df['SMA01'] = price.rolling(window=span01).mean()
    df['SMA02'] = price.rolling(window=span02).mean()
    df['SMA03'] = price.rolling(window=span03).mean()

    plt.figure(figsize=(20, 10))  # グラフのサイズを指定

    # 線グラフ表示
    plt.subplot(2, 1, 1)  # 2行1列のグラフの1番目のグラフを表示
    plt.plot(date, price, label='Close', color='#99b898')  # X軸に日付、Y軸に株価、Closeを表示
    plt.plot(date, df['SMA01'], label='SMA01', color='#e84a5f')  # X軸に日付、Y軸に移動平均線、SMA01を表示
    plt.plot(date, df['SMA02'], label='SMA02', color='#ff847c')  # X軸に日付、Y軸に移動平均線、SMA02を表示
    plt.plot(date, df['SMA03'], label='SMA03', color='#feceab')  # X軸に日付、Y軸に移動平均線、SMA03を表示
    plt.legend()  # 凡例を表示

    # 棒グラフ表示
    plt.subplot(2, 1, 2)  # 2行1列のグラフの2番目のグラフを表示
    plt.bar(date, df['Volume'], label='Volume', color='grey')  # X軸に日付、Y軸に出来高、Volumeを表示

    plt.legend()  # 凡例を表示

    plt.show() # グラフを表示