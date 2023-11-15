#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:10:14 2023

@author: jules
"""

#TD 4 - Time series

#Exercice 1


dates = ["4th January", "5th January", "6th January"]
stock_prices = [155, 156, 153]
for date, price in zip(dates, stock_prices):
                       print(f"{date} : ${price}")


def calculate_average(prices):
    return sum(prices) / len(prices)
average_price = calculate_average(stock_prices)
print(f"Average Stock Price: ${average_price}")

#Exercice 2

def chighest_price(x):
    return max(x)
highest_price=chighest_price(zip(stock_prices, dates)) #attention ici, si l'on inverse, cela prend le max de la première varibale
print(highest_price)

#Exercice 3

stock_prices=stock_prices+[157,152]
dates=dates+["7th January","8th January"]

def analyze_stock_prices(stock_prices):
    if len(stock_prices) < 2:
        return "Not enough data to analyze."

    price_changes = [stock_prices[i] - stock_prices[i - 1] for i in range(1, len(stock_prices))]

    positive_changes = 0
    negative_changes = 0
    zero_changes = 0

    for change in price_changes:
        if change > 0:
            positive_changes += 1
        elif change < 0:
            negative_changes += 1
        else:
            zero_changes += 1

    if positive_changes > negative_changes:
        return "Stock prices are generally increasing."
    elif negative_changes > positive_changes:
        return "Stock prices are generally decreasing."
    else:
        return "Stock prices are generally stable."

#
stock_prices = [155, 156, 153, 157, 152]

result = analyze_stock_prices(stock_prices)

print(result)

#Exercice 1

import statistics as stat
def calculate_volatility(prices):
    return stat.stdev(prices)
volatility = calculate_volatility(stock_prices)
print(f"Volatility: ${volatility}")

#Exercice 2

def average_pri(x):
    return stat.mean(x)

Moyenne_prix = average_pri(stock_prices)
print(Moyenne_prix)

for i in range(1,len(stock_prices)):
    if stock_prices[i] > Moyenne_prix:
        print(f"{dates[i]} : ${stock_prices[i]}")

#Exercice 3

dates2 = ["28th November","29 November","30 November","1st December","2sd December"]
stock_prices2 = [2,4,6,8,10]
for date, price in zip(dates2, stock_prices2):
                       print(f"{date} : ${price}")
                       
def average_c(x):
    if len(x) < 2:
        return "Not enough data to forecast."

    price_changes = [x[i] - x[i - 1] for i in range(1, len(x))]

    
    average_change = sum(price_changes) / len(price_changes)

    last_price = x[-1]
    next_day_forecast = last_price + average_change

    return next_day_forecast

test=average_c(stock_prices2)
print(test)

#Time value of money

def present_value(fv,r,n):
    return fv/(1+r)**n

def future_value (pv,r,n):
    return pv*(1+r)**n

def compound(pv, r):
    return pv * (1 + r)

def discount(fv, r):
    return fv / (1 + r)

#Exercice 1 Given a future value of $120, an interest rate of 5%, and a period of 2 years, calculate the present value.

fv = 120
r = 0.05
n=2

x=present_value(fv, r, n)
print("Present value is:",x)

#Exercice 2 Suppose you’re expecting $500 two years from now. If the discount rate is 6%, what is this amount worth today?

fv = 500
r = 0.06
n=2
x=present_value(fv, r, n)
print("Present value is:",x)

#Exercice 3 How much would a sum of $1000 due 5 years from now be worth today if the interest rate is 4%?

fv=1000
r=0.04
n=5
x=present_value(fv, r, n)
print("Present value is:",x)

#Exercice 1 If you invest $90 today at an interest rate of 7% for a period of 1 year, how much will you have at the end of the year?

pv=90
r=0.07
x=compound(pv,r)
print("Future value is:",x)

#Exercice 2 If you place $200 in a savings account that offers a 3% interest rate com- pounded annually, how much will you have in the account after 2 years?

pv=200
r=0.03
n=2
x=future_value(pv, r, n)
print("Future value is:",x)

#Exercice 3 Given an initial investment of $150 and an annual interest rate of 5%, how much will the investment be worth after 3 years?

pv=150
r=0.05
n=3
x=future_value(pv, r, n)
print("Future value is:",x)

#Exercice 1 If you put $80 in a bank that offers a 9% annual interest rate, how much will you have after compounding for one year?

pv=80
r=0.09
x=compound(pv, r)
print(x)

#Exercice 2 Calculate the present value of $115 that you are to receive one year from now, given an interest rate of 8%.

fv=115
r=0.08
x=discount(fv, r)
print(x)

#Exercice 3 How much do you need to invest today to ensure you have $500 after two years if the annual interest rate is 6%?

fv=500
r=0.06
n=2

x=present_value(fv, r, n)
print(x)

#Exercice 4 If you are promised $180 two years from now and the discount rate is 10%, what is the value of that promise today?

fv=180
r=0.1
n=2

x=present_value(fv, r, n)
print(x)

#Exercice 5 Suppose you can invest money at 7% per annum. How much do you need to invest now to ensure that you will have $1000 three years from now?

fv=1000
r=0.07
n=3
x=present_value(fv, r, n)
print(x)

#Working with Time Series Data using pandas

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Download Apple stock data
apple_data = yf.download("AAPL", start="2020-01-01", end="2023-01-01")
# Display the first few rows of the data
print(apple_data.head())


apple_data['Close'].plot(figsize=(10, 5))
plt.title('Apple Stock Closing Prices')
plt.ylabel('Price in $')
plt.xlabel('Date')
plt.show()


apple_data['50-day MA'] = apple_data['Close'].rolling(window=50).mean()
apple_data[['Close', '50-day MA']].plot(figsize=(10, 5))
plt.title('Apple Stock Prices with 50-day Moving Average')
plt.ylabel('Price in $')
plt.xlabel('Date')
plt.show()

weekly_data = apple_data['Close'].resample('W').mean()
weekly_data.plot(figsize=(10, 5))
plt.title('Apple Stock Weekly Closing Prices')
plt.ylabel("Price in $")
plt.xlabel('Date')
plt.show()

#4.5 Python Exercises for Working with Time Series Data using pandas

#Exercice 1 Fetch the daily stock data of Microsoft (ticker: ”MSFT”) for the year 2021.

microsoft_data = yf.download("MSFT", start="2021-01-01", end="2021-12-31")
print(microsoft_data.head())

#Exercice 2 Retrieve the historical stock price data of Google (ticker: ”GOOGL”) from January 1, 2020, to December 31, 2022.

google_data = yf.download("GOOGL", start="2020-01-01", end="2022-12-31")
print(google_data.head())

#Exercice 3 How would you fetch the stock data of Amazon (ticker: ”AMZN”) for the last quarter of 2021?
amazon_data = yf.download("AMZN", start="2021-10-01", end="2021-12-31")
print(amazon_data.head())

#Exercises related to ”Plotting the closing prices”
#Exercice 1 Plot the daily closing prices of Tesla Inc. (ticker: ”TSLA”) for the year 2020.
tesla_data = yf.download("TSLA", start="2020-01-01", end="2020-12-31")
tesla_data['Close'].plot(figsize=(10, 5))
plt.title('Tesla Stock Closing Prices for 2020')
plt.ylabel('Price in $')
plt.xlabel('Date')        
plt.show()


#Exercice 2 How would you visualize the daily closing prices of Netflix (ticker: ”NFLX”) for the first half of 2022?
netflix_data = yf.download("NFLX", start="2022-01-01", end="2022-06-30")
netflix_data['Close'].plot(figsize=(10, 5))
plt.title('Netflix Closing Prices for the first semester of 2022')
plt.ylabel('Price in $')
plt.xlabel('Date')
plt.show()

#Exercice 3 Generate a plot showcasing the daily closing prices of Facebook (ticker: ”FB”) for the entire year of 2019.
facebook_data = yf.download("NFLX", start="2019-01-01", end="2019-12-31")
facebook_data['Close'].plot(figsize=(10, 5))
plt.title('Facebook Closing Price in2019')
plt.ylabel('Price in $')
plt.xlabel('Date')
plt.show()

#Exercises related to ”Calculating moving averages”

#Exercice 1

ibm_data = yf.download("IBM", start="2020-01-01", end="2021-01-01")
ibm_data['30-day MA'] = ibm_data['Close'].rolling(window=30).mean()
ibm_data[['Close', '30-day MA']].plot(figsize=(10, 5))
plt.title('IBM Stock Prices with 30-day Moving Average 2020')
plt.ylabel('Price (in \$)')
plt.xlabel('Date')
plt.show()

#Exercice 2 Overlay a 20-day moving average on the daily closing prices of Adobe Sys- tems (ticker: ”ADBE”) for the year 2021.

adobe_data = yf.download("ADBE", start="2021-01-01", end="2021-12-31")
adobe_data['20-day MA'] = adobe_data['Close'].rolling(window=20).mean()
adobe_data[['Close', '20-day MA']].plot(figsize=(10, 5))
plt.title('ADOBE Stock Prices with 20-day Moving Average 2021')
plt.ylabel('Price in \$')
plt.xlabel('Date')
plt.show()

#Exercice 3 For Nvidia Corporation (ticker: ”NVDA”) in 2022, visualize the daily closing prices along with its 40-day moving average.

nvidia_data = yf.download("NVDA", start="2022-01-01", end="2022-12-31")
nvidia_data['40-day MA'] = nvidia_data['Close'].rolling(window=40).mean()
nvidia_data[['Close', '40-day MA']].plot(figsize=(10, 5))
plt.title('ADOBE Stock Prices with 20-day Moving Average 2021')
plt.ylabel('Price in \$')
plt.xlabel('Date')
plt.show()

#Exercises related to ”Resampling”

#Exercice 1 Resample the daily closing prices of Starbucks Corp. (ticker: ”SBUX”) in 2020 to get monthly average closing prices.

starbuck_data=yf.download("SBUX",start="2020-01-01",end="2020-12-31")

monthly_data =starbuck_data['Close'].resample('M').mean()
monthly_data.plot(figsize=(10, 5))
plt.title('Starbuck Monthly Closing Price')
plt.ylabel("Price in \$")
plt.xlabel('Date')
plt.show()

#Exercice 2 Resample the daily closing prices of Disney (ticker: ”DIS”) in 2019 to show bi-weekly (every two weeks) average closing prices.

disney_data=yf.download("DIS",start="2019-01-01",end="2019-12-31")

monthly_data =starbuck_data['Close'].resample('2W').mean()
monthly_data.plot(figsize=(10, 5))
plt.title('Disney Bi-weekly Closing Price')
plt.ylabel("Price in \$")
plt.xlabel('Date')
plt.show()

#Exercice 3 For Coca-Cola Company (ticker: ”KO”) in 2020, how would you derive and plot the quarterly average closing prices?

coca_data=yf.download("KO",start="2020-01-01",end="2020-12-31")

quaterly_data =starbuck_data['Close'].resample('Q').mean()
quaterly_data.plot(figsize=(10, 5))
plt.title('Coca-Cola Quaterly Closing Price')
plt.ylabel("Price in \$")
plt.xlabel('Date')
plt.show()






