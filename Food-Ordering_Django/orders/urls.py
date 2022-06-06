from django.urls import path
from . import views
app_name = "orders"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_request, name="login"),
    path("register/", views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("Pizza", views.pizza, name="pizza"),
    path("Pasta", views.pasta, name="pasta"),
    path("Salad", views.salad, name="salad"),
    path("Subs", views.subs, name="subs"),
    path("Drinks", views.drinks, name="drinks"),
    path("Donuts", views.donuts, name="drinks"),
    path("Burger", views.burger, name="drinks"),
    path("Noodles", views.noodles, name="drinks"),
    path("directions", views.directions, name="directions"),
    path("about", views.about, name="about"),
    path("cart", views.cart, name="cart"),
    path("checkout", views.checkout, name="checkout"),
    path("view-orders", views.view_orders, name="view_orders"),
    path("mark_order_as_delivered", views.mark_order_as_delivered, name="mark_order_as_delivered"),
    path("save_cart", views.save_cart, name="save_cart"),
    path("retrieve_saved_cart", views.retrieve_saved_cart, name="retrieve_saved_cart"),
    path("check_superuser", views.check_superuser, name="check_superuser"),

]
