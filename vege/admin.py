from django.contrib import admin
from django.db.models import Sum
# Register your models here.
from .models import *

admin.site.register(Recipe)

