from django.views.generic import ListView

from .models import Order


class OrderListView(ListView):
    model = Order
