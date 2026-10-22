import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

train_df = pd.read_csv(r'C:\Users\USER\Downloads\train.csv')
test_df = pd.read_csv(r'C:\Users\USER\Downloads\test.csv')
features = ['fleet', 'day_index', 'cycle_day', 'slot']
target = 'requests'

X = train_df[features]
y = train_df[target]
x_test = test_df[features]
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

model = XGBRegressor(n_estimators=8000, 
                     learning_rate=0.01, 
                     max_depth=4, 
                     random_state=42, 
                     n_jobs=-1, 
                     early_stopping_rounds=50)
model.fit(X_train, y_train, eval_set=[(X_val, y_val)], verbose=False)

predictions = model.predict(x_test)
predictions = np.maximum(0, predictions)
predictions = np.nan_to_num(predictions, nan=0.0)

submission = pd.DataFrame({
    'id': test_df['id'],
    'requests': predictions
})
submission.to_csv('prediction.csv', index=False)
print(submission.head())

