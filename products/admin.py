from django.contrib import admin
from.models import Items

# Register your models here.
class Itemadmin(admin.ModelAdmin):
    list_display = ("name",'price','stock','image')
admin.site.register(Items,Itemadmin)