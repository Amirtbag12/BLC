from django.urls import path
from .views import cart_view, add_to_cart, update_cart, remove_from_cart, apply_discount, clear_cart ,checkout
from .favourite import add_favourite, remove_favourite, clear_favourite
from .comparison import add_comparison, clear_comparison

urlpatterns = [
    path('', cart_view, name='cart'),
    path('add', add_to_cart, name='add_to_cart' ),
    path('update', update_cart, name='update_cart' ),
    path('remove', remove_from_cart, name='remove_cart' ),
    path('discount', apply_discount, name='discount_apply' ),
    path('clear', clear_cart, name='clear_cart' ),
    path('checkout', checkout, name='checkout' ),
    path('comparison/add', add_comparison, name="add_comparison"),
    path('comparison/clear', clear_comparison, name="clear_comparison"),
    path('favourite/add', add_favourite, name="add_favourite"),
    path('favourite/remove', remove_favourite, name="remove_favourite"),
    path('favourite/clear', clear_favourite, name="clear_favourite"),
]