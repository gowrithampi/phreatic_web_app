# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 15:51:41 2021

@author: gthampi
"""
import scipy.integrate as integrate 
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import seaborn

## function to evaluate the e^-x^2 part of Erfx(lambda)
def efunc(x):
  return math.exp(-math.pow(x,2))

## function to evaluate Erf(lambda), since lambda is a reserved keyword in python, we use l 

def erfc(l): 
  ## evaluate the integral part of erfc, throw away the second result returned, it is an error estimate, irrelevant here
  integral_erfc, _  = integrate.quad(efunc,l,np.inf)
  ## evaluate the constant part of erfc
  const_erfc = 2/math.pow(math.pi,0.5)
  #erfc = const_erfc * integral_erfc
  return integral_erfc



## function to evaluate M of lambda
def M(l,theta):
  return (1 + 2*math.pow(l,2))*erfc(l) - 2/math.pow(theta,0.5)*l*math.exp(-math.pow(l,2))