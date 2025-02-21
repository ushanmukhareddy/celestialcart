from django.urls import path
from app import views

urlpatterns = [
    path('', views.Login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('product/', views.product, name='product'),
    path('cart/', views.cart, name='cart'),
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
    path('login1/', views.login1, name='login1'),
    path('msg/', views.msg, name='msg'),
    path('laptop/', views.laptop, name='laptop'),
    path('pants/', views.pants, name='pants'),
    path('shirts/', views.shirts, name='shirts'),
    path('watches/', views.watches, name='watches'),
    path('mobile/', views.mobile, name='mobile'),
    path('register/', views.register, name='register')
]
