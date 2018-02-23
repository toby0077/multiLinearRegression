# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 17:12:03 2018

@author: Administrator
"""
import pandas as pd
from statsmodels.formula.api import ols

df=pd.read_excel("土壤沉淀物吸收能力采样数据-不存在共线性.xlsx")  

#多元回归函数
def MulitiLinear_regressionModel(df):
    '''Multilinear regression model, calculating fit, P-values, confidence intervals etc.'''
    # --- >>> START stats <<< ---
    # Fit the model
    model = ols("y ~ x1 + x2", df).fit()
    # Print the summary
    print((model.summary()))
    # --- >>> STOP stats <<< ---
    return model._results.params  # should be array([-4.99754526,  3.00250049, -0.50514907])

MulitiLinear_regressionModel(df)
