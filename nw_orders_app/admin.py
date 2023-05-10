from django.contrib import admin

from . import models

admin.site.register(models.FrameProfile)
admin.site.register(models.Wood)
admin.site.register(models.Finish)
admin.site.register(models.PriceKey)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.Spline)