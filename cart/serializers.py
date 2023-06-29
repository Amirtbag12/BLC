from rest_framework import serializers
from .models import Cart, Support

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['user', 'product_id', 'product_title', 'product_title', 'product_collection', 'quantity', 'price', 'image', 'color', 'color_quantity',]
        

class SupportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Support
        fields = ['supporter','support_user','user_message0', 'supporter_message0','user_message1', 'supporter_message1','user_message2', 'supporter_message2','user_message3', 'supporter_message3','user_message4', 'supporter_message4','user_message5', 'supporter_message5','user_message6', 'supporter_message6','user_message7', 'supporter_message7','user_message8', 'supporter_message8','user_message9', 'supporter_message9','user_message10', 'supporter_message10','user_message11', 'supporter_message11','user_message12', 'supporter_message12','user_message13', 'supporter_message13','user_message14', 'supporter_message14','user_message15', 'supporter_message15','user_message16', 'supporter_message16','user_message17', 'supporter_message17','user_message18', 'supporter_message18','user_message19', 'supporter_message19','support_status',]
