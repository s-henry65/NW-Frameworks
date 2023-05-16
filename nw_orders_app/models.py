from django.db import models
from nw_users_app.models import UserProfile
from django.contrib.auth.models import User

class PriceKey(models.Model):
    profile_style = models.CharField(max_length=30)
    image = models.ImageField(blank=True)
    width_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.profile_style + ', ' + str(self.width_price)

class FrameProfile(models.Model):
    description = models.CharField(max_length=30, blank=True)
    number = models.CharField(max_length=20)
    image = models.ImageField(blank=True)
    width_quarters = models.DecimalField(max_digits=10, decimal_places=1)
    category = models.ForeignKey(PriceKey, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.number + ', ' + self.description
    
    class Meta:
        ordering = ('number',)

class Wood(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=20, blank=True)
    image = models.ImageField(blank=True)
    price_modifier = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name + ', ' + str(self.price_modifier)
    
    class Meta:
        ordering = ('name',)

class Spline(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=20, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

class Finish(models.Model):
    name = models.CharField(max_length=30, blank=True)
    number = models.CharField(max_length=20)
    image = models.ImageField(blank=True)
    price_modifier = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.number + ', ' + str(self.price_modifier)
    
    class Meta:
        ordering = ('number',)

class Order(models.Model):
    customer = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    order_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    notes = models.CharField(max_length=300, blank=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    frame_total = models.IntegerField(null=True, blank=True)
    order_delivered = models.BooleanField(default=False)
    order_paid = models.BooleanField(default=False)
    archive = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ', ' + str(self.customer) + ', ' + str(self.order_date)
    
    class Meta:
        ordering = ('order_date',)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(FrameProfile, on_delete=models.SET_NULL, null=True)
    depth = models.IntegerField()
    wood = models.ForeignKey(Wood, on_delete=models.SET_NULL, null=True)
    spline = models.ForeignKey(Spline, on_delete=models.SET_NULL, null=True)
    finish = models.ForeignKey(Finish, on_delete=models.SET_NULL, null=True)
    width = models.FloatField()
    height = models.FloatField()
    price_ui = models.DecimalField(max_digits=10, decimal_places=2)
    ui = models.DecimalField(max_digits=10, decimal_places=2)
    frame_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.profile} , {self.width} x {self.height}'
    
    @property
    def get_total(self):
        total = self.frame_price * self.quantity
        return total