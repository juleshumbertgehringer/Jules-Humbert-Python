#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 17:28:44 2023

@author: jules
"""

#TD3 - Class, Objet, Attribute, Method

#Classes - exercice 1

class Bond:
    def __init__(self, par_value, coupon_rate, maturity):
        self.par_value = par_value
        self.coupon_rate = coupon_rate
        self.maturity = maturity
    def current_yield(self, market_price):
        return (self.coupon_rate * self.par_value) / market_price
ten_year_note = Bond(1000, 0.025, 10)
yield_on_note = ten_year_note.current_yield(950)
print(yield_on_note)

class Stock:
    def __init__(self, stock_name,current_price,dividend):
        self.stock_name = stock_name
        self.current_price=current_price
        self.dividend=dividend
    def yield_dividend(self): #on crée en quelque sorte une fonction nommée yield_dividend
        return self.dividend/self.current_price
total_stock = Stock("Total",61.28 , 3.51)
print(total_stock.yield_dividend())

#Exercice 2

class Securities:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Portfolio:
    def __init__(self):
        self.Securities = []  # stockage matrice 1*n

    def add_instrument(self, instrument):
            self.Securities.append(instrument)
    def total_value(self):
        total = 0
        for instrument in self.Securities:
            total += instrument.price
        return total

stock1 = Securities("AAPL", 150.0)
stock2 = Securities("Total", 61.28)
bond = Securities("US Bond", 1000.0)

portfolio = Portfolio()
portfolio.add_instrument(stock1)
portfolio.add_instrument(stock2)
portfolio.add_instrument(bond)

total_portfolio_value = portfolio.total_value()
print(total_portfolio_value)

#Exercice 3

class CurrencyConverter:
    def __init__(self, currencyA, currencyB, conversion_rates):
        self.currencyA = currencyA
        self.currencyB = currencyB
        self.conversion_rates = conversion_rates
    
    def convert(self, amount):
        if self.currencyA in self.conversion_rates and self.currencyB in self.conversion_rates:
            rate_A_to_B = self.conversion_rates[self.currencyB] / self.conversion_rates[self.currencyA]
            converted_amount = amount * rate_A_to_B
            return converted_amount
        else:
            return "Conversion rates not available for the specified currencies."


conversion_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.72,
    "JPY": 112.35
}

converter = CurrencyConverter("USD", "EUR", conversion_rates)
amount_in_usd = 100.0
converted_amount = converter.convert(amount_in_usd)
print(f"{amount_in_usd} USD is equivalent to {converted_amount} EUR")


#exemple de numpy

import numpy as np
prices = np.array([100, 102, 104, 101, 99, 98])
returns = (prices[1:] - prices[:-1]) / prices[:-1]
print("Daily returns:", returns)
annual_volatility = np.std(returns) * np.sqrt(252)  # Assuming 252 trading days
print("Annualized volatility:", annual_volatility)

#ex 1

np.random.seed(0) # For reproducibility
daily_returns = np.random.normal(0.001, 0.02, 1000) ;stock_prices = [100]
for r in daily_returns :
    stock_prices.append(stock_prices[-1] * (1 + r)) ;print(stock_prices[-1])

#ex 2 portfolio variance

import numpy as np

sigma1 =0.1
sigma2 =0.2
rho=0.5
w1=0.6
w2=0.4

variance=w1**w1*sigma1**sigma1+w2**w2*sigma2**sigma2+2*w1*w2*sigma1*sigma2*rho
print(variance)

#ex 3 Efficience frontier

import numpy as np

# Given annual returns and volatilities
returns = np.array([0.10, 0.15])  # Annual returns for Asset A and Asset B
volatilities = np.array([0.20, 0.30])  # Annual volatilities (standard deviations) for Asset A and Asset B

# Define a range of weight combinations
weights = np.linspace(0, 1, 11)  # Create 11 weight combinations from 0% to 100% in 10% increments

# Initialize lists to store portfolio returns and volatilities
portfolio_returns = []
portfolio_volatilities = []

# Calculate portfolio returns and volatilities for different weight combinations
for w in weights:
    weight_vector = np.array([w, 1 - w])  # Weight vector for the portfolio
    portfolio_return = np.dot(weight_vector, returns)
    portfolio_volatility = np.sqrt(np.dot(weight_vector, np.dot(np.diag(volatilities), weight_vector.T)))
    
    portfolio_returns.append(portfolio_return)
    portfolio_volatilities.append(portfolio_volatility)

# Print the calculated returns and volatilities for a few weight combinations
print("Weight Combination | Portfolio Return | Portfolio Volatility")
for i in range(len(weights)):
    print(f"{weights[i]:.2f} | {portfolio_returns[i]*100:.2f}% | {portfolio_volatilities[i]*100:.2f}%")
    

#Data vizualization tools
%matplotlib inline 
import matplotlib.pyplot as plt
import seaborn as sns

stock_prices = [100, 102, 104, 103, 105, 107, 108]
dates = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
plt.figure(figsize=(10, 6))
sns.lineplot(x=dates, y=stock_prices)
plt.title('stock price over a week')
plt.xlabel('Days')
plt.ylabel('stock price')
plt.grid(True)
plt.show()

#ex 1
%matplotlib inline
import matplotlib.pyplot as plt

# Stock prices for the first stock
stock_prices1 = [105, 103, 106, 109, 108, 107, 110, 112, 111, 113]

# Stock prices for the second stock
stock_prices2 = [107, 108, 107, 107, 106, 108, 109, 108, 109, 110]

# Plot the first stock with a blue line
plt.plot(stock_prices1, label='Stock A', color='blue')

# Plot the second stock with a red line
plt.plot(stock_prices2, label='Stock B', color='red')

plt.title('Stock Prices Over 10 Days')
plt.xlabel('Days')
plt.ylabel('Stock Price')

# Add a legend to differentiate between the two stocks
plt.legend()

plt.show()

#ex 2

import matplotlib.pyplot as plt
import seaborn as sns
returns = [0.05, -0.02, 0.03, -0.01, 0.02, 0.03, -0.03, 0.01, 0.04, -0.01]
sns.histplot(returns, bins=5, kde=True)
plt.title('Distribution of Stock Returns')
plt.show()









        
        



                
