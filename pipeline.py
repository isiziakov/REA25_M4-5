import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.metrics import root_mean_squared_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
from catboost import CatBoostRegressor
import pickle
import time
import os
from sklearn.multioutput import MultiOutputRegressor

# Получение текущей директории
current_directory = os.getcwd()
print(f"Текущая директория: {current_directory}")

# Обход всех поддиректорий и файлов
for root, dirs, files in os.walk(current_directory):
    print(f"Текущая папка: {root}")
    for dir in dirs:
        print(f"Поддиректория: {dir}")
    for file in files:
        print(f"Файл: {file}")

print('start')

def pipeline2(train_X, train_y, val_X, val_y):
    X = pd.read_csv(train_X, header=None, nrows=5)
    y = pd.read_csv(train_y, header=None, nrows=5)
    print("load1")
    valX = pd.read_csv(val_X, header=None, nrows=5)
    valy = pd.read_csv(val_y, header=None, nrows=5)
    print("load2")

    model = MultiOutputRegressor(CatBoostRegressor(verbose=False))

    stime = time.time()
    model.fit(X, y)
    print("fit")
    predict = model.predict(valX)
    print("predict")
    dct = {
        "Время обучения и предсказания": time.time() - stime,
        "R2": r2_score(valy, predict),
        "RMSE": root_mean_squared_error(valy, predict),
        "MSE": mean_squared_error(valy, predict),
        "MAE": mean_absolute_error(valy, predict),
        "MAPE": mean_absolute_percentage_error(valy, predict),
    }

    return model, dct

path = "data/"
model, dct = pipeline2(path + "data_X.csv", path + "data_y.csv", path + "data_X_val.csv", path + "data_y_val.csv")

with open(path + 'model.pkl', 'wb') as file:
    pickle.dump(model, file)

with open(path + 'metrics.txt', 'w') as file:
    for key, value in dct.items():
        file.write(f'{key}: {value}\n')
