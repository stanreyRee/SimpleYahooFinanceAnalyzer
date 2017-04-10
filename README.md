# Simple Yahoo Finance Analyzer (Python)
## Description
This is a simple finance analyzer that uses data gathered from Yahoo Finance. It downloads stock data from Yahoo Finance according to user's input. It provides two simple indicators to analyze the historical stock information, and using different strategies to provide primary suggestions of when to buy/sell the stock they are tracking.



## About Indicatiors
### There are two indicators being used in this project: the 'Simple Moving Average Indicator', and the 'Directional Indicator'. 
#### Simple Average Indicator 
Simple Average Indicator keeps track of stock price in a specific period of time, get the average stock price, and compare the stock price of the last day of the period with the average. If the last day's stock price is above the average, we set the indicator as '+'; if the price falls below the average, we set the indicator as '-'. We leave it blank when two prices are the same.


#### Directional Indicator
Directional Indicator records the change of stock price in a similar way. Except that it indicates how many days the stock prices keeps raising/failing. The indicator will keep track of each day's stock price comparing to the previous day, recording 1 for raising price, -1 for failing price, and 0 otherwise. Then in a 'sliding' period (e.g. period 1 is day 1 to day 7, and period 2 is day 2 to day 8), it will get the average of the recorded number in this specific period, and assign it to the relative days.

The indicators are used to make sell and buy suggestions. The indicators listed above have their own way to analyze the stock information.



### Strategy for Simple Average Indicator
In this strategy, the analyzer checks on the indicator lists to find the switch between '+' and '-'. If there is a switch from '+' to '-', the analyzer suggests to SELL the stock; if the stock price switches from '-' to '+', the suggestion will be to BUY the stock.

### Strategy for Directional Indicator
In this strategy, the analyzer will keep track of the indicator to see if the indicator is above/below the user-given sell/buy signals. If the indicator is above the sell signal, analyzer suggests to SELL the stock, and suggests to BUY if the indicator falls below the buy signal.



## FYI
- This is an academic project for non-commercial use.
- This is a polished version of the original one. The original one was finished on 02/20/2013.
