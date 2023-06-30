from django.urls import path
import .views as main


urlpatterns = [
    path('', main.index, name='monitor'),
]