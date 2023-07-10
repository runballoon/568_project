import django_tables2 as tables
from .models import Stocks, Overviews
from django.utils.html import format_html

class StockTable(tables.Table):
    company = tables.Column(verbose_name='Company')
    ticker = tables.Column(verbose_name='Ticker')
    current = tables.Column(verbose_name='Current Price')
    one_pred = tables.Column(verbose_name='1-Day Prediction')
    one_pred_diff = tables.Column(verbose_name='1-Day Trend')
    three_pred = tables.Column(verbose_name='3-Day Prediction')
    three_pred_diff = tables.Column(verbose_name='3-Day Trend')
    seven_pred = tables.Column(verbose_name='7-Day Prediction')
    seven_pred_diff = tables.Column(verbose_name='7-Day Trend')

    def render_current(self, value):
        return '${:.2f}'.format(value)

    def render_one_pred(self, value):
        return '${:.2f}'.format(value)

    def render_three_pred(self, value):
        return '${:.2f}'.format(value)

    def render_seven_pred(self, value):
        return '${:.2f}'.format(value)

    def render_one_pred_diff(self, value):
        up_color='#14A44D'
        down_color='#DC4C64'
        color=''
        if value>=0:
            color=up_color
        else:
            color=down_color
        return format_html('<span style="color:{}">{}%</span>', color, '{:.2f}'.format(value*100))

    def render_three_pred_diff(self, value):
        up_color = '#14A44D'
        down_color = '#DC4C64'
        color = ''
        if value >= 0:
            color = up_color
        else:
            color = down_color
        return format_html('<span style="color:{}">{}%</span>', color, '{:.2f}'.format(value * 100))

    def render_seven_pred_diff(self, value):
        up_color = '#14A44D'
        down_color = '#DC4C64'
        color = ''
        if value >= 0:
            color = up_color
        else:
            color = down_color
        return format_html('<span style="color:{}">{}%</span>', color, '{:.2f}'.format(value * 100))

    class Meta:
        model = Stocks
        template_name = "django_tables2/bootstrap.html"
        fields = ("company", "ticker", "current", "one_pred", "one_pred_diff", "three_pred", "three_pred_diff")


class OverviewTable(tables.Table):
    def render_open(self, value):
        return '${:.2f}'.format(value)

    def render_high(self, value):
        return '${:.2f}'.format(value)

    def render_low(self, value):
        return '${:.2f}'.format(value)

    def render_close(self, value):
        return '${:.2f}'.format(value)

    def render_adjclose(self, value):
        return '${:.2f}'.format(value)

    class Meta:
        model = Overviews
        template_name = "django_tables2/bootstrap.html"
        fields = ("company", "ticker", "date", "open", "high", "low", "close", "adjclose", "volume")