from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Items(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default= User.pk)
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://www.shutterstock.com/image-illustration/coming-soon-concept-image-text-600nw-2402613961.jpg")
    
    def __str__(self) -> str:
        return self.item_name
        # return super().__str__() It returns "id" of the object
        
    def get_absolute_url(self):
        
        return reverse('food:detail', kwargs={'pk': self.pk})