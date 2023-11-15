#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pricing d'une option et d'un call sur le modèle de Black-Merton-Scholes. L'objectif étant
après de l'utiliser pour réaliser un produit structuré. Bonus : réaliser les graphiques PayOff
"""


import yfinance as yf
from datetime import date
from scipy.stats import norm
import numpy as np

taux = yf.download('^FVX',start=date.today(),end=None)
#print(taux)

def BS_call(S,K,T,r,sigma):
    
    d1 = (np.log(S/K)+(r-sigma**2/2)*T)/(r*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    
    call_price = S*norm.cdf(d1)-K*np.exp(-r*T)*norm.cdf(d2)
    return call_price

def BS_put(S,K,T,r,sigma):
    d1 = (np.log(S/K)+(r-sigma**2/2)*T)/(r*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    
    put_price = K*np.exp(-r*T)*norm.cdf(-d2)-S*norm.cdf(-d1)
    return put_price

S=7200;K=7500;T=1;r=0.045;sigma=0.20

put_price = BS_put(S,K,T,r,sigma)

call_price = BS_call(S,K,T,r,sigma)

print("Put price is : ",put_price)
print("Call price is : " , call_price)

"""
#if call_price - put_price == S - K*np.exp(-r*T):
#    print("call_price is: ",call_price,"put price is: ",put_price)
#else:
#    print("error") ébauche de vérification de la parity call/put
"""


"""On détermine ci-dessous la part de l'investissement que l'on doit allouer au zero coupon bond
1y pour garantir le capital au bout de 5 ans. Puis on construit un produit structuré avec un 
gain x2 si le CAC40 monte, garanti 100% du capital sinon.

Pour ce faire, on achète 2 call, qu'on price avec la fonction ci-dessus. La marge est réalisée
sur le capital non employé"""

amount_invested = 30000
invested_bond = amount_invested*np.exp(-r*T)
part = invested_bond/amount_invested
#print(invested_bond)
print("Part = ",part)

remaining_amount = amount_invested - invested_bond
#print(remaining_amount)
if remaining_amount >= 2*call_price:
    print("We can make this structured projet")
    margin = (amount_invested - invested_bond - 2*call_price)/amount_invested
    print(margin)
else:
    print("This structured product is unrealistic")
    









   


    
    
    







