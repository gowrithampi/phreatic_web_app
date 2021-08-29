# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 14:25:53 2021

@author: gthampi
"""
import pandas as pd
import streamlit as st
import scipy.integrate as integrate 
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import seaborn
import helper_functions as hf


st.title("Sample App : Phreatic Line")


### Some written content ## 

st.markdown("Implementation of Equation 6 from \
Phreatic Line Calculation and Stability Analysis of Slopes under the Combined Effect of Reservoir Water Level Fluctuations and Rainfall by Guanhua Sun, Yongtao Yang, Shengguo Cheng, Hong Zheng1")


st.markdown("As the first step we calculate ")

st.latex('''
         Erfc(\lambda) = \frac{2}{\sqrt(\pi)}\int_\lambda^\infty e^{-x^2} dx
         ''')

st.markdown("We then evaluate")
st.latex(r'''
         M(\lambda) = (1 + 2\lambda^2)Erfc(\lambda) - \frac{2}{\sqrt(\theta)}\lambda{e}^{-\lambda^2}
         ''')

theta = st.slider('theta', 0, 90) 
l = st.slider('lambda', 0, 5)

try: 
     M =  hf.M(l,theta)
except ZeroDivisionError : 
    M = 'zero division error please choose another value'
M


#@title Plotting M(Lambda) 
## Plotting M of lambda against lambda for different values of theta

fig, ax = plt.subplots()
## this is an array of lambda values for which we are plotting the graph
## the first argument is start, the point at which we are starting, the second is stop
## the third is the step size, a smaller step size will give a smoother graph
## feel free to modify these and redraw
l_array = np.arange(start = 0,stop = 2,step = 0.01)

M_array =[hf.M(el,20) for el in l_array]

plt.plot(l_array, M_array)


