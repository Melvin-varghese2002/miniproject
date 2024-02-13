from django.contrib import admin
from.models import Recipe_add
# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['Item_name','Recipe','Image']
admin.site.register(Recipe_add,RecipeAdmin)
