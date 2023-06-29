from wagtail.admin.menu import MenuItem
from django.urls import path, reverse
from .views import daily_visit_view
from wagtail import hooks


@hooks.register('register_admin_urls')
def register_daily_visit():
    return [
        path('daily_visit', daily_visit_view, name='daily_visits'),
    ]

@hooks.register('register_admin_menu_item')
def register_daily_visit_item():
    return MenuItem('پشتیبانی بر خط', reverse('daily_visits'), icon_name='tablet-alt')