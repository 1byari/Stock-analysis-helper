# Stock Analysis Helper

### Author: Oleksandr Popovych
### Institution: ČVUT–FIT
### Email: popovole@fit.cvut.cz
### Date: May 26, 2024

## Introduction

Stock Analysis Helper is a project designed to aid in the analysis of financial markets using data visualization technology on the Dash platform by Plotly.

## Features

### 1. Display Current Stock Prices
- Displays the closing prices of stocks on the exchange.

### 2. Stock and Indicator Selection
- Users can select stocks and indicators from a dropdown menu.

### 3. Technical Indicator Analysis

#### 3.1 Moving Average (MA)
- Moving averages are typically used with time series data to smooth out short-term fluctuations and highlight longer-term trends or cycles.

#### 3.2 Relative Strength Index (RSI)
- RSI uses an exponential averaging method and a specific formula to map price movements on a scale from 0 to 100, clearly showing the real value of each price change.

#### 3.3 Moving Average Convergence-Divergence (MACD)
- MACD uses two moving averages of different lengths to determine the direction and duration of a trend (main and signal lines). The histogram shows the difference between the lines. Positive values of the main and signal lines characterize a rising trend, while negative values indicate a falling trend.

#### 3.4 Swing
- The swing indicator measures the percentage change in the stock price over a given time interval, allowing identification of short-term trends and market fluctuations.

#### 3.5 Candlestick Pattern Analysis
- Candlestick models display a range of price information such as open price, close price, high, and low prices, using graphical symbols shaped like candles, each providing a concise overview of trading activity over a certain period.

### 4. Time Interval Selection for Analysis
- Users can choose start and end dates for the analysis, allowing detailed exploration of market trends.

### 5. News Analysis
- The application provides news for selected stocks and analyzes the sentiment of the news articles using an NLP pipeline to determine the overall mood.

## Technical Implementation

- The application is designed using Dash and Plotly.
- Flask cache is used for news to improve performance and reduce the number of API queries.
- Stock data is loaded via the yfinance library, which is based on the Yahoo Finance API.
- News is fetched using the News API.

## Challenges

- A major challenge is the limitation of free API services for obtaining news. The News API allows access to news from only the past month and lacks deep filtering, significantly affecting the quality of information. With more powerful news retrieval tools, the usefulness of the news analysis feature would greatly increase. Additionally, the project is not ready for high loads and requires improvements to handle requests from a large number of users (in such cases, it would be better to switch from Dash to a more powerful web framework).

## Project Potential

This project has significant development potential. Only a small percentage of various indicators for analysis have been covered, and the number of companies has been artificially limited.

## Conclusion

The "Stock Analysis Helper" can significantly aid users in analyzing market trends. The developed application allows users not only to track current quotes but also to analyze financial markets using various indicators and news analysis.