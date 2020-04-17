from django.shortcuts import render
from django.views.generic import ListView

from ordering_system.models import Order


class OrdersListView(ListView):
    model = Order
    context_object_name = 'orders'
    ordering = ['-time']
    template_name = 'admin_orders/order_list.html'
