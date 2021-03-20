from django.contrib import admin

# Register your models here.
from api.models import Journal, Book

admin.site.register(Book)
admin.site.register(Journal)
