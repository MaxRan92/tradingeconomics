'''
Importing libraries
'''
import tradingeconomics as te
from datetime import datetime, timedelta
import json
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import DeleteView, UpdateView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from requests.exceptions import Timeout, TooManyRedirects, RequestException, HTTPError  # noqa
import pandas as pd
import pandas_market_calendars as mcal

# Create your views here.


class CountryDetails(view):

    te.login()
    
