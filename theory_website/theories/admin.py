from django.contrib import admin
from .models import Theory

@admin.register(Theory)
class TheoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')
