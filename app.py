# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 14:25:53 2021

@author: gthampi
"""
import pandas as pd
import streamlit as st
#import plotly.express as px

st.title("Sample App : Phreatic Line")

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
