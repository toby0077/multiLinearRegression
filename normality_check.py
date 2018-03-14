# -*- coding: utf-8 -*-
'''
Author：Toby
QQ：231469242，all right reversed,no commercial use
normality_check.py
正态性检验脚本
  
'''
  
import scipy
from scipy.stats import f
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
# additional packages
from statsmodels.stats.diagnostic import lillifors
  
#对一列数据进行正态分布测试
def check_normality(testData):
    print("one group normality check begin:")
    #20<样本数<50用normal test算法检验正态分布性
    if 20<len(testData) <50:
       p_value= stats.normaltest(testData)[1]
       if p_value<0.05:
           print("use normaltest")
           print("p value:",p_value)
           print ("data are not normal distributed")
           return  False
       else:
           print("use normaltest")
           print("p value:",p_value)
           print ("data are normal distributed")
           return True
      
    #样本数小于50用Shapiro-Wilk算法检验正态分布性
    if len(testData) <50:
       p_value= stats.shapiro(testData)[1]
       if p_value<0.05:
           print ("use shapiro:")
           print("p value:",p_value)
           print ("data are not normal distributed")
           return  False
       else:
           print ("use shapiro:")
           print("p value:",p_value)
           print ("data are normal distributed")
           return True
        
    if 300>=len(testData) >=50:
       p_value= lillifors(testData)[1]
       
       if p_value<0.05:
           print ("use lillifors:")
           print("p value:",p_value)
           print ("data are not normal distributed")
           return  False
       else:
           print ("use lillifors:")
           print("p value:",p_value)
           print ("data are normal distributed")
           return True
      
    if len(testData) >300:
       p_value= stats.kstest(testData,'norm')[1]
       if p_value<0.05:
           print ("use kstest:")
           print("p value:",p_value)
           print ("data are not normal distributed")
           return  False
       else:
           print ("use kstest:")
           print("p value:",p_value)
           print ("data are normal distributed")
           return True
    #测试结束
    print("-"*100)
  
#对所有样本组进行正态性检验
def NormalTest(list_groups):
    for group in list_groups:
        #正态性检验
        status=check_normality(group)
        if status==False :
            return False
              
 

group1=[5,2,4,2.5,3,3.5,2.5,3]
group2=[1.5,2,1.5,2.5,3.3,2.3,4.2,2.5]
group3=[96,90,95,92,95,94,94,94]
list_groups=[group1,group2,group3]
list_total=group1+group2+group3
#对所有样本组进行正态性检验  
NormalTest(list_groups)
