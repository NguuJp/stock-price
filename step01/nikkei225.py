from pandas_datareader import data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import yfinance as yf

# # 「pandas_datareader」の処理を更新する
yf.pdr_override()

# 銘柄コード入力(^N225は日経225の株価です。)
ticker_symbol = "^N225"

# 2022-01-01以降の株価取得
start = '2019-01-01'
end = dt.date.today()

# データ取得
df = data.get_data_yahoo(ticker_symbol, start, end)

date = df.index
price = df['Adj Close']

# 移動平均線の計算
span01 = 5
span02 = 25
span03 = 50
df['SMA01'] = price.rolling(window=span01).mean()
df['SMA02'] = price.rolling(window=span02).mean()
df['SMA03'] = price.rolling(window=span03).mean()

plt.figure(figsize=(30, 15))  # グラフのサイズを指定
# 線グラフ表示
plt.subplot(2, 1, 1)  # 2行1列のグラフの1番目のグラフを表示
plt.plot(date, price, label='Nikkei225', color='grey')  # X軸に日付、Y軸に株価、Nikkei225を表示
plt.plot(date, df['SMA01'], label='SMA01', color='#e84a5f')  # X軸に日付、Y軸に移動平均線、SMA01を表示
plt.plot(date, df['SMA02'], label='SMA02', color='#ff847c')  # X軸に日付、Y軸に移動平均線、SMA02を表示
plt.plot(date, df['SMA03'], label='SMA03', color='#feceab')  # X軸に日付、Y軸に移動平均線、SMA03を表示
plt.title('Nikkei225', color='white', backgroundcolor='grey', size=40, loc='center')  # グラフタイトル
# plt.xlabel('Date', color='black', size=30)  # X軸ラベル
# plt.ylabel('Price', color='black', size=30)  # Y軸ラベル

# 棒グラフ表示
plt.subplot(2, 1, 2)  # 2行1列のグラフの2番目のグラフを表示
plt.bar(date, df['Volume'], label='Volume', color='grey')  # X軸に日付、Y軸に出来高、Volumeを表示
plt.title('Nikkei225', color='white', backgroundcolor='grey', size=40, loc='center')  # グラフタイトル

plt.legend()  # 凡例を表示


plt.show()

