from django.contrib import admin

# Register your models here.
from .models import CatColour, CatSpecies, Cat

admin.site.register(CatColour)
admin.site.register(CatSpecies)
admin.site.register(Cat)