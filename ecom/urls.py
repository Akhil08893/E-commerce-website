from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register,name='register'),
    path('product/<int:pk>',views.product,name='product'),
    path('category/<str:c>',views.category,name='category'),
    path('user_profile/',views.user_profile,name='user_profile'),
    path('change_password/',views.change_password,name='change_password'),
    path('user_address/',views.user_profile,name='user_address'),
    path('search_product/',views.search_product,name='search_product')
]