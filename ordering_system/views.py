import json
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import Pizza, Customer, Order


def home(request):
    context = {
        'pizzas': Pizza.objects.all()
    }
    return render(request, 'ordering_system/index.html', context)


def cart(request):
    return render(request, 'ordering_system/cart.html')


def place_order_rest(request):
    if request.method == 'POST':
        response_data = request.body.decode('utf-8')
        data = json.loads(response_data)
        cart_items = data['cartItems']
        order_info = data['orderInfo']
        # Grab all the pizzas with from database and compute total amount
        pizzas = Pizza.objects.all()
        amount = 0.0
        cart_items_str = ''
        for item in cart_items:
            item_price = 0.0
            pizza = pizzas.filter(id=item['id'])[0]
            if item['size'] == 'large':
                item_price = pizza.large_price
            if item['size'] == 'regular':
                item_price = pizza.regular_price
            if item['size'] == 'small':
                item_price = pizza.small_price
            item_price = item_price * item['quantity']
            amount += item_price
            cart_items_str += f'{item["quantity"]}x {item["size"]} ' \
                              f'{item["flavour"]} \n'
        # Create a new customer, order object and save it in database
        try:
            customer = Customer.objects.get(email=order_info['email'])
        except Customer.DoesNotExist:
            customer = Customer.objects.create(name=order_info['name'],
                                               email=order_info['email'],
                                               address=order_info['address'])
        time = datetime.now()
        Order.objects.create(customer=customer, amount=amount,
                             items=cart_items_str,
                             time=time,
                             instructions=order_info['instructions'])
        # Sending order through websocket to room 'admin_orders_list'
        ws_order = {
            'items': cart_items_str,
            'instructions': order_info['instructions'],
            'amount': amount,
            'time': time.isoformat(),
        }
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'admin_orders_list',
            {
                'type': 'send_order',
                'order': ws_order
            }
        )

        return HttpResponse(status=200)
    return HttpResponse('BAD REQUEST', status=404)
