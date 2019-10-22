from django.contrib import admin
from .models import BasicPerson
from users.models import  Employee


# Register your models here.

admin.site.register(BasicPerson)
admin.site.register(Employee)
