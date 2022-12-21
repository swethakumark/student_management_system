from django.contrib import admin
from .models import Contact,Course,Coursedeatils,Staff

# Register your models here.

class Customerdetails(admin.ModelAdmin):
    list_display=('name','phno','email')
admin.site.register(Contact,Customerdetails)
admin.site.register(Course)
admin.site.register(Coursedeatils)
admin.site.register(Staff)

