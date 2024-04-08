from django.contrib import admin
from .models import order,OrderItem

admin.site.register(order)

admin.site.register(OrderItem)
