from django.urls import path
from . import views

urlpatterns = [
    path('ownerview/', views.OwnerShops, name='ownerview'),
    path('addshop/', views.AddShop, name='addshop'),
    path('userview/', views.ShopUserHome, name='userview'),
    path('inshop/<int:id>', views.itemqueryview, name='inshop'),
    path('appoinment/<int:id>', views.appoinmentview, name='appoinment'),
    path('search/', views.search, name='search'),
]
