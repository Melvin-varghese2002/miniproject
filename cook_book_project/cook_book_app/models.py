from django.db import models

# Register your models here.
class Recipe_add(models.Model) :
    Item_name=models.CharField(max_length=300)
    Recipe=models.CharField(max_length=2000)
    Image=models.ImageField(upload_to='None')

    def __str__(self) :
        return self.Item_name