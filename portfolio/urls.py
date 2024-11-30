from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.portfolio_view, name='portfolio_view'),
    path('add/', views.add_stock, name='add_stock'),
    path('remove/<int:stock_id>/', views.remove_stock, name='remove_stock'),
]
