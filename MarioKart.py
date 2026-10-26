import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from scipy.interpolate import UnivariateSpline
from catboost import CatBoostRegressor

train_df = pd.read_csv(r"D:\python\train2.csv")
test_df = pd.read_csv(r"D:\python\test2.csv")

def create_advanced_features(df):
    X = pd.DataFrame()
    X['id'] = df['id']
    
    time_cols = [f'time_{i}' for i in range(1, 7)]
    disp_cols = [f'displacement_{i}' for i in range(1, 7)]
    obj_cols = [f'nearest_object_{i}' for i in range(1, 7)]
    
    X['query_time'] = df['query_time']
    X['time_gap'] = df['query_time'] - df['time_6']
    
    speeds = []
    for i in range(1, 6):
        dt = df[f'time_{i+1}'] - df[f'time_{i}']
        dd = df[f'displacement_{i+1}'] - df[f'displacement_{i}']
        dt = np.where(dt == 0, 1e-5, dt)
        speed = dd / dt
        X[f'speed_{i}_{i+1}'] = speed
        speeds.append(speed)
        
    speeds_df = pd.DataFrame(speeds).T
    X['mean_speed'] = speeds_df.mean(axis=1)
    X['std_speed'] = speeds_df.std(axis=1)
    X['last_speed'] = speeds_df.iloc[:, -1]
    
    X['linear_pred'] = df['displacement_6'] + (X['last_speed'] * X['time_gap'])
    
    spline_preds = []
    for idx, row in df.iterrows():
        times = [row[c] for c in time_cols]
        disps = [row[c] for c in disp_cols]
        try:
            spl = UnivariateSpline(times, disps, k=2, s=0)
            pred = spl(row['query_time'])
            spline_preds.append(pred)
        except:
            spline_preds.append(row['displacement_6'])
            
    X['spline_pred'] = spline_preds
    
    X['path_signature'] = (
        df['nearest_object_1'].astype(str) + '_' + 
        df['nearest_object_2'].astype(str) + '_' + 
        df['nearest_object_3'].astype(str) + '_' + 
        df['nearest_object_4'].astype(str) + '_' + 
        df['nearest_object_5'].astype(str) + '_' + 
        df['nearest_object_6'].astype(str)
    )
    
    for col in time_cols + disp_cols:
        X[col] = df[col]
        
    for col in obj_cols:
        X[col] = df[col].astype(str)
        
    categorical_features = obj_cols + ['path_signature']
    
    return X, categorical_features

X_train_raw, cat_features = create_advanced_features(train_df)
X_test_raw, _ = create_advanced_features(test_df)

features_to_use = [c for c in X_train_raw.columns if c != 'id']
X = X_train_raw[features_to_use]
y = train_df['target_displacement']
X_test = X_test_raw[features_to_use]

X_tr, X_val, y_tr, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

model = CatBoostRegressor(
    iterations=3000,
    learning_rate=0.03,
    depth=6,
    cat_features=cat_features,
    random_seed=42,
    early_stopping_rounds=100,
    thread_count=-1,
    silent=True
)

model.fit(
    X_tr, y_tr,
    eval_set=(X_val, y_val)
)

final_preds = model.predict(X_test)
final_preds = np.clip(final_preds, 0, None)

submission = pd.DataFrame({
    'id': test_df['id'],
    'target_displacement': final_preds
})
print(submission.head(5))
submission.to_csv('mario prediction', index=False)