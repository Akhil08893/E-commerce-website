from django.urls import path
from . import views

urlpatterns = [
    path('payment_success',views.payment_success,name='payment_success'),
    path('check_out',views.check_out,name='check_out'),
]