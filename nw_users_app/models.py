from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_num = models.CharField(max_length=20)
    email = models.EmailField()
    shop_name = models.CharField(max_length=50)
    shop_address = models.CharField(max_length=50)
    shop_city = models.CharField(max_length=20)
    shop_state = models.CharField(max_length=20)
    shop_zipcode = models.CharField(max_length=15)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.shop_name + ', ' + self.first_name + ' ' + self.last_name
    
    class Meta:
        ordering = ('shop_name',)

# class Retailer(models.Model):
#     shop_name = models.CharField(max_length=50)
#     shop_address = models.CharField(max_length=50)
#     shop_city = models.CharField(max_length=20)
#     shop_state = models.CharField(max_length=20)
#     shop_zipcode = models.CharField(max_length=15)
#     phone_num = models.CharField(max_length=20)
#     website = models.URLField(blank=True)
    
#     def __str__(self):
#         return self.shop_name + ', ' + self.shop_city + ', ' + self.shop_state
    
#     class Meta:
#         ordering = ('shop_name',)