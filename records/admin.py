from django.contrib import admin

# Register your models here.
from .models import Cardiology, Endocrinology


admin.site.register(Cardiology)
admin.site.register(Endocrinology)

