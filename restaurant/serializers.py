from rest_framework import serializers
from .models import Menu , Booking

class MenuItemSerializer (serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','Name','No_of_guests','BookingDate']

""""
class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory','category','category_id']
"""