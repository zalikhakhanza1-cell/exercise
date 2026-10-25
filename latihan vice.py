import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# 1. Load dataset
train_df = pd.read_csv(r'C:\Users\USER\Downloads\train.csv')
test_df = pd.read_csv(r'C:\Users\USER\Downloads\test.csv')

# 2. Tentukan fitur dan target
features = ['fleet', 'day_index', 'cycle_day', 'slot']
target = 'requests'

X = train_df[features]
y = train_df[target]
X_test = test_df[features]

# Split data training menjadi data latih dan data validasi untuk mengukur MAE
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.1, random_state=22)

# 3. Training model Random Forest
print("Melatih model...")
model = XGBRegressor(
    n_estimators=2000,   # Jumlah pohon ditingkatkan agar lebih teliti
    learning_rate=0.01,   # Kecepatan belajar dibuat lebih lambat tapi akurat
    max_depth=4,          # Kedalaman pohon dibatasi agar tidak overfitting
    random_state=42,      # mengunci jumlah sampel
    n_jobs=-1,           # memrintahkan laptop memakai seluruh inti prosesor
    early_stopping_rounds=30) # Berhenti jika dalam 50 putaran skor MAE tidak membaik
# model.fit(X_train, y_train)
model.fit(X_train, y_train, eval_set=[(X_val, y_val)],
    verbose=False)

#4. Evaluasi model menggunakan MAE pada data validasi
val_predictions = model.predict(X_val)
val_mae = mean_absolute_error(y_val, val_predictions)
print(f"Skor MAE pada data validasi: {val_mae:.4f}")

# # 6. Prediksi data test
# print("Membuat prediksi untuk test.csv...")
predictions = model.predict(X_test)

# Aturan kompetisi: Angka harus non-negatif dan tidak boleh NaN[cite: 3]
predictions = np.maximum(0, predictions)
predictions = np.nan_to_num(predictions, nan=0.0)

# 7. Buat file submission.csv dengan tepat 2 kolom: id dan requests[cite: 3]
submission = pd.DataFrame({
    'id': test_df['id'],
    'requests': predictions
})

submission.to_csv('latihan vice.csv', index=False)
# print("Berhasil! File 'submission.csv' sudah dibuat dan siap dikirim.")
print(submission.head())
