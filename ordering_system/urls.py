from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import home, cart, place_order_rest


urlpatterns = [
    path('', home, name='ordering-system-home'),
    path('cart/', cart, name='ordering-system-cart'),
    path('order/', place_order_rest, name='ordering-system-order-rest-view'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

