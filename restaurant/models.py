from django.db import models


# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(max_length=6)
    BookingDate = models.models.DateTimeField()
    
    def __str__(self): 
        return self.Name


# Add code to create Menu model
class MenuItem(models.Model):
   Title = models.CharField(max_length=200) 
   price = models.models.DecimalField( max_digits=10, decimal_places=2,null=False) 
   Inventory = models.models.IntegerField(max_length=5)
   
   def __str__(self):
       return f'{self.title} : {str(self.price)}'