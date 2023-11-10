# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:27:46 2023

@author: Sushitha Devaraju
"""
#importing libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#from a csv file    
market = pd.read_csv('supermarket_sales.csv')
#taking the first 15 elements from the data
market1 = market.head(15)
    
#defining the function for piechart
def plot(place):
    plt.pie(market1[place].value_counts().values, labels=market1[place].value_counts().index, autopct='%1.1f%%')
    
#adding title and legend   
    plt.title('Supermarket Sales of Three Cities',fontsize=15)
    plt.legend(loc=2 ,bbox_to_anchor=(1,1))
    plt.show()
    
#calling the function for piechart    
plot('city')