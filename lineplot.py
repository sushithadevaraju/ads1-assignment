# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 18:23:49 2023

@author: Sushitha Devaraju
"""
#importing libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#from a csv file
nod= pd.read_csv('noodles.csv')

#taking the first 5 elements from the data
nod1= nod.head(5)

#defining the function for linechart
def lineplot(place,col_a,col_b,col_c,col_d,col_e):
    plt.plot(nod1[place],nod1[col_a],label=col_a,linewidth=2)
    plt.plot(nod1[place],nod1[col_b],label=col_b,linewidth=2)
    plt.plot(nod1[place],nod1[col_c],label=col_c,linewidth=2)
    plt.plot(nod1[place],nod1[col_d],label=col_d,linewidth=2)
    plt.plot(nod1[place],nod1[col_e],label=col_e,linewidth=2)
    
#adding x and y labels    
    plt.xlabel('Country',fontsize=15)
    plt.ylabel('Consumption',fontsize=15)
    
#addng title and legend 
    plt.title('Consumption of Noodles from 2018-2022',fontsize=20)   
    plt.legend()
    plt.show()  
    
#calling the function for linechart     
lineplot('Country/Region','2018','2019','2020', '2021','2022')