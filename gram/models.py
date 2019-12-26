from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='pictures/')
    bio = models.CharField(max_length=300)

class Image(models.Model):
    Image = models.ImageField(upload_to = 'pictures/')
    name = models.CharField(max_length=50)
    caption = models.CharField(max_length=300)
    user = models.ForeignKey(Profile,on_delete = models.CASCADE)
    


