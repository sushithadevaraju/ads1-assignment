# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:18:56 2023

@author: Sushitha Devaraju
"""
#importing libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#from a csv file
sal = pd.read_csv('Salary.csv')

#defining the function for barchart
def barchart(col_a,col_b,label_a,label_b,):
    plt.figure()
    plt.bar(sal[col_a],sal[col_b],width=0.3,label=label_a)
    
#adding x and y labels    
    plt.xlabel('Country',fontsize=15)
    plt.ylabel('Salary',fontsize=15)
    
#addng title and legend   
    plt.title('Salary Range Across Various Countries', fontsize=18)
    plt.legend(prop={'size':8})
    plt.show()
    
#calling the function for barchart    
barchart('Country','Salary','Country','Salary')  