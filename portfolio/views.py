from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm  # We'll create this form next
from django.http import HttpResponse
import requests

def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            # Save the stock to the database
            stock = form.save()

            # Fetch real-time stock price (using an API)
            fetch_current_price(stock)

            return redirect('portfolio:portfolio_view')
    else:
        form = StockForm()
    return render(request, 'portfolio/add_stock.html', {'form': form})

def remove_stock(request, stock_id):
    stock = Stock.objects.get(id=stock_id)
    stock.delete()
    return redirect('portfolio:portfolio_view')

def portfolio_view(request):
    stocks = Stock.objects.all()
    return render(request, 'portfolio/portfolio.html', {'stocks': stocks})



def fetch_current_price(stock):
    API_KEY = 'NBOOQI8HVRVFIVL4'
    url = f'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': stock.symbol,
        'interval': '5min',
        'apikey': API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()
    if 'Time Series (5min)' in data:
        latest_data = list(data['Time Series (5min)'].values())[0]
        current_price = latest_data['4. close']
        stock.current_price = current_price
        stock.save()

