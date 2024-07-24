# machine/urls.py

from django.urls import path
from .views import BeverageListView, DispenseBeverageView, InventoryListView, InventoryDetailView

urlpatterns = [
    # Endpoint to get a list of all beverages
    path('beverages/', BeverageListView.as_view(), name='beverage-list'),
    # Endpoint to dispense a beverage
    path('beverages/dispense/', DispenseBeverageView.as_view(), name='dispense-beverage'),
    # Endpoint to get the inventory status
    path('inventory/', InventoryListView.as_view(), name='inventory-list'),
    # Endpoint to update a single ingredient by its ID
    path('inventory/<int:pk>/', InventoryDetailView.as_view(), name='inventory-detail'),
]
