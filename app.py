import strealit as st
import io
import requests
import numpy as np
from sklearn import metrics
import os
import json
import csv
import pandas as pd


train_data = pd.read_csv("./dataset/trainingData.csv")

st.dataframe(train_data, 200, 100)



