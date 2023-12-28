from django.contrib import admin

# Register your models here.

from .models import Booking, Review, Customer, ToolItem

admin.site.register(Customer)
admin.site.register(ToolItem)
admin.site.register(Booking)
admin.site.register(Review)

