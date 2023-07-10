from django.urls import path, re_path, include

from apps.stock.views import StockListView, OverviewListView, about_view
# from django.apps import apps as cache
#
# if not cache.loaded:
#     cache.get_models()

urlpatterns = [
    path("stock/", StockListView.as_view()),
    path("overview/", OverviewListView.as_view()),
    path("about/", about_view),
]