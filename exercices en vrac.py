#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create an int variable representing the total number of shares you want
to purchase and a float variable representing the share price. Calculate
the total investment amount.
"""

from pprint import pprint

number_shares = int(6)
share_price = 13.45
amount_invested = number_shares * share_price
#print(amount_invested)

#[08:20] LANDI, Alexandre-EXT Take a stock price in float and convert it into an int by rounding itto the nearest whole number

share_price=round(share_price)
#print(share_price)

""" Create string variables for a company’s name, its ticker, and CEO. Display
them in a single sentence."""

apple = "APPL"
ceo = "Tim Cook"
#print('The company is',apple,'and it has',ceo,'as ceo')
#print(f'The company {apple} is led by {ceo}')


"""Simulate a simplistic credit rating downgrade: if a variable bond rating
is a string ”AAA”, change it to ”AA+”."""

bond_rating = "AAA"
bond_rating = "AA+"
#print(bond_rating)

"""Create a list of at least three stock tickers. Then, add a new ticker to the
list and remove the second ticker in the list."""

#ok

"""dictionary"""

dictionary={'sticker':'APPL','price':100,'volume':3000}
dictionary.update({'test':6})
dictionary["outstanding_shares"]=43
#print(dictionary)

"""Use a list to store daily closing prices of a stock for a week. Calculate the
average closing price."""

closing_price = [10,20,30,40,9]
moyenne=sum(closing_price)/len(closing_price)
print(moyenne)

"""Create a dictionary where the keys are tickers and the values are another
dictionary containing stock information (price, market cap, sector). Re-
trieve information for a specific ticker."""

dictionary={"APPL":{"price":180,'market cap':3000000000,"sector":"new technologies"},
            "STBK":{"price":80,'market cap':7000,"sector":"coffee"}}
pprint(dictionary["APPL"])

"""You have two lists: one with stock tickers and another with corresponding
daily gains/losses. Convert these into a dictionary with tickers as keys
and daily movements as values"""

#ce n'est pas ça mais cool

# list_stock={"APPL","AMZN","STBK"}
# daily_return={100,-60,50}

# for sticker, rreturn in zip(list_stock,daily_return):
#     print(f'{sticker}:${rreturn}')

"""Given a list of stock prices throughout a week, write a ’for’ loop that
calculates and prints the price change from the previous day, for each day
after the first."""

# list_stock_prices=[10,15,7,8,5]
# i=1
# while i<len(list_stock_prices):
#     daily_return=list_stock_prices[i]-list_stock_prices[i-1]
#     i+=1
#     print(daily_return)

# print(list(range(2,8)))

# s=0
# while s<10:
#     s+=1
# print(s)

    
    




