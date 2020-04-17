from django.urls import path

from .views import OrdersListView


urlpatterns = [
    path('list/', OrdersListView.as_view(), name='admin_orders_list'),
]
