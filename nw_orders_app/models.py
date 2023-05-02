from django.db import models

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

class Finish(models.Model):
    name = models.CharField(max_length=30, blank=True)
    number = models.CharField(max_length=20)
    image = models.ImageField(blank=True)
    price_modifier = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.number + ', ' + str(self.price_modifier)
    
    class Meta:
        ordering = ('number',)