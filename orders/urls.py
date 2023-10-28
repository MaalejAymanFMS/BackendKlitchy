from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_orders", views.get_orders, name="get_orders"),
    path("add_order", views.add_order, name="add_order"),
    path("update_order", views.update_order, name="update_order"),
]
