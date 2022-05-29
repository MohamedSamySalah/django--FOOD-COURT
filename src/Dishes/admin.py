from django.contrib import admin
from .models import category,Dishes,Resturants
# Register your models here.

admin.site.register(category)
admin.site.register(Dishes)
admin.site.register(Resturants)

admin.site.site_header = 'FOOD COURT'
admin.site.site_title = 'FOOD COURT'


class ResturantsAdmin(admin.ModelAdmin):

    pass