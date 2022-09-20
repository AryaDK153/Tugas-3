from django.urls import path
from mywatchlist.views import show_watchlist

app_name = 'watchlist'

urlpatterns = [
    path('', show_watchlist, name='show_watchlist'),
]