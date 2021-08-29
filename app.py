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

#import plotly.express as px
theta = float(input("Enter the value of theta: "))
l = float(input("Enter the value of lambda: "))
print("The value of M(lambda) is {M_:.2f}".format(M_ = hf.M(l,theta)))

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


