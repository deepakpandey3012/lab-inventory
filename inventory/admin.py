from django.contrib import admin

# Register your models here.
from .models import Floor
from .models import Categorie
from .models import Item
from .models import Room

# Register your models here.



admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(Categorie)
admin.site.register(Item)
