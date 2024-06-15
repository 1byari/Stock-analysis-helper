# Project description

Stock Analysis Helper is a project designed to aid in the analysis of financial markets using data visualization technology on the Dash platform by Plotly.

## Features

### 1. Display Current Stock Prices
- Displays the closing prices of stocks on the exchange.

### 2. Stock and Indicator Selection
- Users can select stocks and indicators from a dropdown menu.

### 3. Technical Indicator Analysis

#### 3.1 Moving Average (MA)
- Moving averages are typically used with time series data to smooth out short-term fluctuations and highlight longer-term trends or cycles.

![screenshot_ma](https://github.com/1byari/Stock-analysis-helper/assets/74068520/5359fc15-dd5a-4e44-bf7d-6fe31b3b07cd)


#### 3.2 Relative Strength Index (RSI)
- RSI uses an exponential averaging method and a specific formula to map price movements on a scale from 0 to 100, clearly showing the real value of each price change.

![screenshot_rsi](https://github.com/1byari/Stock-analysis-helper/assets/74068520/1cbbe9e1-e7fd-46bb-9870-a6d137a25c59)


#### 3.3 Moving Average Convergence-Divergence (MACD)
- MACD uses two moving averages of different lengths to determine the direction and duration of a trend (main and signal lines). The histogram shows the difference between the lines. Positive values of the main and signal lines characterize a rising trend, while negative values indicate a falling trend.

![screenshot_macd](https://github.com/1byari/Stock-analysis-helper/assets/74068520/11c72509-27f2-486d-bfd6-b1e338a3273e)

#### 3.4 Swing
- The swing indicator measures the percentage change in the stock price over a given time interval, allowing identification of short-term trends and market fluctuations.

![screenshot_swing](https://github.com/1byari/Stock-analysis-helper/assets/74068520/d0337c66-2d20-4463-af66-ce22ab2b11f9)


#### 3.5 Candlestick Pattern Analysis
- Candlestick models display a range of price information such as open price, close price, high, and low prices, using graphical symbols shaped like candles, each providing a concise overview of trading activity over a certain period.

![screenshot_candles](https://github.com/1byari/Stock-analysis-helper/assets/74068520/609bc429-a103-4103-b77e-5f17258e6583)

### 4. Time Interval Selection for Analysis
- Users can choose start and end dates for the analysis, allowing detailed exploration of market trends.

### 5. News Analysis
- The application provides news for selected stocks and analyzes the sentiment of the news articles using an NLP pipeline to determine the overall mood.

<img width="288" alt="screenshot_news" src="https://github.com/1byari/Stock-analysis-helper/assets/74068520/4e11f934-4163-47bf-b79f-6dc533d2628a">


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



# How to use this project 

## Prerequisites

Ensure you have Python 3.8+ installed on your system

## Installation ##

1. **Clone the repository**:
2. **Install the dependencies**:
`pip install -r requirements.txt`


## Running the Application
Execute the following command in the app directory of the project:
`python run.py`

Navigate to the url provided by Dash in your web browser to view the app.

## Testing ##

**Make sure you have chromedriver installed locally**

Execute the following command in the root directory of the project:
`pytest`

## Usage ##
- Selecting Tickers and Indicators: Use the dropdown menus to select the stock tickers and the financial indicators you want to analyze.
- Adjusting Date Ranges: Pick start and end dates to define the period for your stock data.
- Viewing News Sentiments: Click on the 'Load News' button to fetch and display sentiment analysis results for the selected ticker.









