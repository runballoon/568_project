import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import  r2_score
import datetime as dt
from yahoo_fin.stock_info import *

class LSTM:
    def __init__(self, ticker):
        self.window = 5
        self.future = 1
        self.split_ratio = 0.8
        self.ticker = ticker
        self.start_date = dt.date.today() - dt.timedelta(days=1000)
        self.end_date = None
        self.index_as_date = True
        self.interval = "1d"
        self.model_path_to_artifacts = f"myjoblib/{ticker}.joblib"
        self.model = joblib.load(self.model_path_to_artifacts)
        self.sc = StandardScaler()
        self.new_sc = StandardScaler()
        self.Xy_data = None
        self.Xy_nm = None
        self.X_test = None
        self.y_test = None
        self.future_pred_X = None
        self.future_pred_y = None

    def split(self, data, window, future=1):
        X, y = [], []
        for i in range(len(data) - window + 1 - future + 1):
            X.append(data[i:i + window - 1, :])
            y.append(data[i + window - 1 + future - 1, :])
        return np.array(X), np.array(y)

    def preproccess(self):
        self.Xy_data = get_data(self.ticker, self.start_date, self.end_date, self.index_as_date, self.interval).iloc[:, :4]
        self.Xy_nm = self.sc.fit_transform(self.Xy_data.values)
        self.Xy_nm = pd.DataFrame(data=self.Xy_nm, index=self.Xy_data.index, columns=self.Xy_data.columns)
        X_split, y_split = self.split(self.Xy_nm.values, self.window, self.future)
        split_idx = int(len(X_split) * self.split_ratio)
        X_train, self.X_test = X_split[:split_idx], X_split[split_idx:]
        y_train, self.y_test = y_split[:split_idx], y_split[split_idx:]

    def predict(self, data):
        return self.model.predict(data)

    def setSc(self):
        self.new_sc.scale_, self.new_sc.mean_, self.new_sc.var_ = self.sc.scale_[-1], self.sc.mean_[-1], self.sc.var_[-1]

    def future_pred(self):
        self.setSc()
        self.future_pred_X = np.array([self.Xy_nm.values[(-1) * self.window + 1 + (-1) * self.future + 1:, :]])
        self.future_pred_y = self.predict(self.future_pred_X)
        return self.new_sc.inverse_transform(self.future_pred_y)

    def pred_accu(self):
        y_pred=self.predict(self.X_test)
        return r2_score(self.y_test, y_pred)

    def compute_prediction(self, duration):
        future_pred_X_1 = self.future_pred_X
        future_pred_y_1 = self.future_pred_y
        for i in range(duration - 1):
            future_pred_X_1 = np.block([[[future_pred_X_1[0][1:]], [future_pred_y_1]]])
            future_pred_y_1 = self.predict(future_pred_X_1)
        return self.new_sc.inverse_transform(future_pred_y_1)

    def postprocessing(self, duration):
        prediction = self.future_pred()
        if duration>1:
            prediction = self.compute_prediction(duration)
        return {"probability": self.pred_accu(), "prediction": prediction, "status": "OK"}

    def update_model(self):
        self.preproccess()
        X = np.array([self.Xy_nm.values[(-1) * self.window + (-1) * self.future + 1:-1, :]])
        y = np.array([self.Xy_nm.values[-1:, :]])
        self.model.fit(X, y, batch_size=4, epochs=50, verbose=2, shuffle=False)
        joblib.dump(self.model, self.model_path_to_artifacts, compress=True)

    def current(self):
        return self.Xy_data[-1:].values[0][-1]
