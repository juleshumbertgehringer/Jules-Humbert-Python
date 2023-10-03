#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 15:01:13 2023

@author: jules
"""

import numpy as np
import pandas as pd

#exercice 1.1

ticker = "AAPL"
opening_price = 142.7
closing_price = 143.2
volume = 1200000
print(ticker, opening_price, closing_price,volume)

#exercice 1.2

currency_pair = 'EUR/USD'
buying_rate = 1.1825
celling_rate = 1.1830
currency_exchange = [currency_pair,buying_rate,celling_rate]
print(currency_exchange)

#exercice 1.3

stocks = ['AAPL','MSFT','GOOGL']
IBM = ['IBM']
new_stocks = stocks + IBM
print(new_stocks)
#ou avec la fonction stocks.append('IBM')

#Exercice 1.4

stocks_add = ["TSLA","AMZN","FB"]
stocks_add.append("NVDA");stocks_add.append("AMD")
print(stocks_add)

#exercice 1.5

stock_dictionary = {'ticker':'AAPL','opening_price':142.7,'closing_price' : 1.1830,'volume':1200000}
print(stock_dictionary)

bond_dictionary = {'issuer':'France','maturity date':'','coupon rate' : 0.05,'face value':1200000}
print(bond_dictionary)

#Loops, for loops excercice 1
stock_prices = [105, 107, 105, 106, 103]
somme = 0
for i in range(1, len(stock_prices)):
   daily_return = (stock_prices[i] - stock_prices[i-1]) / stock_prices[i]
   somme += daily_return
   #équivalent à somme = somme + daily_return
   print("daily_return",daily_return)
#modification of the code to have the average return over the enterie period
moyenne = somme/len(stock_prices)
print("moyenne",moyenne)
   

#Loops while, exercice 3


principal = 500
rate = 0.07
years = 0
while principal < 1000:
             principal *= (1 + rate)
             #équivalent à principal = principal * (1+rate)
             years += 1
print(years)
#modify the code to print the final value of investment after those years

future_value = principal*(1+rate)**years
print("FV=",future_value)

#if,

bond_yield = 4.5

if bond_yield > 4.5:
    print("Buy the bond.")

#elif and else,

pe_ratio = 20

if pe_ratio < 15:
    print("Buy the stock.")
elif pe_ratio >= 15 and pe_ratio <= 25:
    print("Hold the stock.")
else:
    print("Sell the stock.")
    





