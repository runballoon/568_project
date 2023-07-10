"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

application = get_wsgi_application()

# import inspect
# from apps.ml.registry import MLRegistry
# from apps.ml.income_classifier.lstm import LSTM
#
# try:
#     registry = MLRegistry() # create ML registry
#     # Random Forest classifier
#     lstm = LSTM("azn")
#     # add to ML registry
#     registry.add_algorithm(endpoint_name="income_classifier",
#                             algorithm_object=lstm,
#                             algorithm_name="LSTM",
#                             algorithm_status="production",
#                             algorithm_version="0.0.1",
#                             owner="YG",
#                             algorithm_description="LSTM",
#                             algorithm_code=inspect.getsource(LSTM))
#
# except Exception as e:
#     print("Exception while loading the algorithms to the registry,", str(e))