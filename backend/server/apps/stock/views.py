from django.shortcuts import render
from django_tables2 import SingleTableView

from .models import Stocks, Overviews
from .tables import StockTable, OverviewTable

from pytickersymbols import PyTickerSymbols
import datetime as dt
from yahoo_fin.stock_info import *

from apps.ml.income_classifier.lstm import LSTM

class StockListView(SingleTableView):
    model = Stocks
    table_class = StockTable
    template_name = 'stock.html'

    stock_data = PyTickerSymbols()
    nasdaq_100_stocks = stock_data.get_nasdaq_100_nyc_yahoo_tickers()
    company_d = dict()

    today = dt.date.today()
    for x in stock_data.get_stocks_by_index('NASDAQ 100'):
        company_d[x['symbol']] = x['name']
    for ticker in nasdaq_100_stocks:
        if Stocks.objects.filter(ticker=ticker).exists():
            continue
        company_name="" if ticker not in company_d else company_d[ticker]
        lstm = LSTM(ticker)
        lstm.preproccess()
        current=round(lstm.current(), 2)
        one_pred=round(lstm.future_pred()[0][-1], 2)
        three_pred=round(lstm.compute_prediction(3)[0][-1], 2)
        seven_pred=round(lstm.compute_prediction(7)[0][-1], 2)
        one_pred_diff=round(one_pred / current-1, 4)
        three_pred_diff = round(three_pred / current - 1, 4)
        seven_pred_diff = round(seven_pred / current - 1, 4)
        x=Stocks(company=company_name, ticker=ticker, current=current, one_pred=one_pred, three_pred=three_pred, update_time=today,
                 one_pred_diff=one_pred_diff, three_pred_diff=three_pred_diff, seven_pred_diff=seven_pred_diff)
        x.save()

    for ticker in nasdaq_100_stocks:
        if Stocks.objects.filter(ticker=ticker, update_time=today).exists():
            continue
        lstm = LSTM(ticker)
        lstm.update_model()
        one_pred = round(lstm.future_pred()[0][-1], 2)
        three_pred = round(lstm.compute_prediction(3)[0][-1], 2)
        Stocks.objects.filter(ticker=ticker).update(one_pred=one_pred, three_pred=three_pred)


class OverviewListView(SingleTableView):
    model = Overviews
    table_class = OverviewTable
    template_name = 'overview.html'

    stock_data = PyTickerSymbols()
    nasdaq_100_stocks = stock_data.get_nasdaq_100_nyc_yahoo_tickers()
    company_d = dict()

    today = dt.date.today()
    for x in stock_data.get_stocks_by_index('NASDAQ 100'):
        company_d[x['symbol']] = x['name']
    for ticker in nasdaq_100_stocks:
        if Overviews.objects.filter(ticker=ticker).exists():
            continue
        company_name = "" if ticker not in company_d else company_d[ticker]
        try:
            data=get_data(ticker, today, None)
        except:
            x = Overviews(company=company_name, ticker=ticker, date=today)
            x.save()
        else:
            date=data.index.date[0]
            open=data.values[0][0]
            high=data.values[0][1]
            low=data.values[0][2]
            close=data.values[0][3]
            adjclose=data.values[0][4]
            volume=data.values[0][5]
            x=Overviews(company=company_name, ticker=ticker, date=date, open=open, high=high, low=low, close=close, adjclose=adjclose, volume=volume)
            x.save()

    for ticker in nasdaq_100_stocks:
        if Overviews.objects.filter(ticker=ticker, date=today).exists():
            continue
        try:
            data = get_data(ticker, today, None)
        except:
            Overviews.objects.filter(ticker=ticker).update(date=today, open=None, high=None, low=None, close=None, adjclose=None, volume=None)
        else:
            date = data.index.date[0]
            open = data.values[0][0]
            high = data.values[0][1]
            low = data.values[0][2]
            close = data.values[0][3]
            adjclose = data.values[0][4]
            volume = data.values[0][5]
            Overviews.objects.filter(ticker=ticker).update(date=date, open=open, high=high, low=low, close=close, adjclose=adjclose, volume=volume)

def about_view(request):
    return render(request, 'about.html')