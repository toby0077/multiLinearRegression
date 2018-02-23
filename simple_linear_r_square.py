# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 11:35:50 2018

@author: Administrator
"""
import pandas as pd
import scipy.stats as stats


df=pd.read_excel("工农业产值与货运量-存在共线性.xlsx")  
array_values=df.values
x1=[i[0] for i in array_values]
x2=[i[1] for i in array_values]
y=[i[2] for i in array_values]
sample=len(x1)


print("use Pearson,parametric tests x1 and x2")
r,p=stats.pearsonr(x1,x2)
print("pearson r**2:",r**2)
print("pearson p:",p)
if sample<30:
    print("when sample <30,pearson has no mean")
print("-"*100)
    
print("use Pearson,parametric tests x1 and y")
r,p=stats.pearsonr(x1,y)
print("pearson r**2:",r**2)
print("pearson p:",p)
if sample<30:
    print("when sample <30,pearson has no mean")    
print("-"*100)

    
print("use Pearson,parametric tests x2 and y")
r,p=stats.pearsonr(x2,y)
print("pearson r**2:",r**2)
print("pearson p:",p)
if sample<30:
    print("when sample <30,pearson has no mean")       
print("-"*100)    
    
    
    
    
    
    
    
    
    
    
    