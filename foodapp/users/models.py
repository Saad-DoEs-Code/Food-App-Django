from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    
    user = models.OneToOneField(to=User, on_delete= models.CASCADE)
    image = models.ImageField(default="https://cdn-icons-png.flaticon.com/512/149/149071.png",upload_to="profile_pictures")
    location = models.CharField(max_length=100)
