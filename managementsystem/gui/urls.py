from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='gui-index'),
    path('staff/', views.staff, name='gui-staff'),
    path('orders/', views.orders, name='gui-orders'),
    path('orders/delete/<int:key>/', views.delete_order, name='gui-orders-delete'),
    path('orders/update/<int:key>/', views.update_order, name='gui-orders-update'),
    path('orders/mail/<int:key>/', views.mail_order, name='gui-orders-mail'),
    ]