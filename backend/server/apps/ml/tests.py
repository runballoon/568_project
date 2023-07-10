from django.test import TestCase
import joblib
import numpy as np
import pandas as pd
import datetime as dt
from yahoo_fin.stock_info import *
from apps.ml.income_classifier.lstm import LSTM
import inspect
# from apps.ml.registry import MLRegistry
from pytickersymbols import PyTickerSymbols

class MLTests(TestCase):
    def test_lstm(self):
        stock_data = PyTickerSymbols()
        nasdaq_100_stocks = stock_data.get_nasdaq_100_nyc_yahoo_tickers()
        # preds=[]
        for ticker in nasdaq_100_stocks:
            model=LSTM(ticker)
            model.preproccess()
            # preds.append(model.future_pred()[0][-1])
            # print(model.pred_accu())
            model.future_pred()
            print(model.compute_prediction(3))
        # print(preds)

    # def test_registry(self):
    #     registry = MLRegistry()
    #     self.assertEqual(len(registry.endpoints), 0)
    #     endpoint_name = "income_classifier"
    #     algorithm_object = LSTM("AZN")
    #     algorithm_name = "lstm"
    #     algorithm_status = "production"
    #     algorithm_version = "0.0.1"
    #     algorithm_owner = "YG"
    #     algorithm_description = "LSTM"
    #     algorithm_code = inspect.getsource(LSTM)
    #     registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
    #                            algorithm_status, algorithm_version, algorithm_owner,
    #                            algorithm_description, algorithm_code)
    #     self.assertEqual(len(registry.endpoints), 1)
