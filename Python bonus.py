#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 12:34:01 2023

@author: jules
"""

#Basic Practice exercises
#Exercise 1
total_shares=1000
print(type(total_shares))
share_price = 23.75
print(type(share_price))

def total_investment(x,y):
    return x*y

print(total_investment(total_shares, share_price))

#Exercise 2

rates = 4.5

def convert(x):
    return float(x/100)

print(convert(rates))

#Exercice 3
#on reprend share_price

rounding=round(share_price)
print(rounding)

#Exercise 4

name="Facebook"
sticker="FB"
CEO="Zuckerberg"

print("The company",name,"whose the sticker is",sticker,"has mister",CEO,'as the CEO')

#Exercise 5 for a 1-year coupon bond

bond_rating="AAA"
discount_rate = 0.04
par_value=1000
coupon_rate=0.08
market_value = (par_value*(1+coupon_rate))/(1+discount_rate)


if bond_rating=="AA+":
    coupon_rate = 0.10
    market_value=(par_value*(1+coupon_rate))/(1+discount_rate)
    
print(market_value)

#Exercise on collection

#Exercise 1

List=[1,2,3]
List.append(6)
List.pop(1)
print(List)

#Exercise 2

Dictionary=stock_info = [{
    "ticker": "AAPL",
    "price": 150.25,
    "volume": 1000000,
    "shares_outstanding": 5000000
},{"ticker": "FB",
"price": 13.25,
"volume": 3000000,
"shares_outstanding": 7000000}]

print(Dictionary[0])

#Exercise 3

Total_return=0

Closing_price=[20,30,45,34,25,12]
for i in range(1,len(Closing_price)):
    Daily_return=(Closing_price[i]-Closing_price[i-1])/Closing_price[i]
    Total_return=Total_return+Daily_return

Average_return = Total_return/len(Closing_price)
print(Average_return)

#Exercise 4

Dictionarycarré={"FB":{"price":13,"cap":19000000,"sector":"Social Media"},
                 "AAPL":{"price":40,"cap":5000000,"sector":"Hard- and software"}}

print(Dictionarycarré["FB"])

#Exercise 5

stock_tickers=["FB","APPL","NFLX","TTL"]
daily_changes=[-0.3,0.5,5,-7]

Newdictionary=dict(zip(stock_tickers,daily_changes))

print(Newdictionary)

#Exercise on Loop

#Exercise 1
daily_changes=0
u=[12,12.5,11.33,14.66,11.9]
for i in range(1,len(u)):
    daily_changes=u[i]-u[i-1]
    print(daily_changes)
    
#Exercise 2
v={"FB":150,"APPL":200,"AMZN":300}
for key, value in v.items():
    print(key,":",value)

#Exercise 3 

Budget = 1000
stock_price = 100
i=0
while Budget>=stock_price:
    Budget-=stock_price
    i+=1

print(i)

#Exercise 4

interest_rates=[0.3,0.4,0.66,0.78,0.97]
investment=1000
for i in range(1,len(interest_rates)):
    compound_invest=investment*(1+interest_rates[i-1])
    print(compound_invest)
    
#Exercise 5
import numpy as np
somme=0
w=np.random.rand(30)*100
print(w)
for i in range(1,len(w)):
    somme=somme+w[i-1]
average_price=somme/len(w)
print(average_price)
while average_price > 45:
    max_index = np.argmax(w)
    w = np.delete(w, max_index)
    average_price = np.mean(w)
    
print(len(w))



#Exercise on conditionnal loop

#Exercise 1

loan_score = 670


if loan_score > 700:
    print("We accept the loan")
elif 650 < loan_score < 700:
    n = input("Do you agree to accept the loan? ")
    if n == "yes":
        print("We accept the loan")
    else:
        print("We refuse the loan")
else:
    print("We refuse the loan")


        




    



