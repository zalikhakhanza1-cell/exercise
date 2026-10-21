import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

train_df = pd.read_csv(r'C:\Users\USER\Downloads\train.csv')
test_df = pd.read_csv(r'C:\Users\USER\Downloads\test.csv')
features = ['fleet', 'day_index', 'cycle_index', 'slot']
target = 'request'

X = train_df[features]
y = train_df[target]
x_test = test_df[features]
