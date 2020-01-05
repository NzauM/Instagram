from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='pictures/')
    bio = models.CharField(max_length=300)
    username = models.CharField(max_length=50,default='Your username')

    def __str__(self):
        return self.username

    def search_user(cls,username):
        found_user = User.objects.get(username = username)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Image(models.Model):
    ig_pic = models.ImageField(upload_to= 'pictures/')
    name = models.CharField(max_length=50)
    caption = models.CharField(max_length=300)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes' ,blank=True,)
    

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def all_images(cls):
        timeline_pics = cls.objects.all()
        return timeline_pics

    @classmethod
    def user_pics(cls,user):
        user_pic = cls.objects.filter(user = user)
        return user_pic

    @classmethod
    def one_pic(cls,id):
        one_pic = cls.objects.filter(id = ig_pic_id)
        return one_pic


    @property
    def all_likes(self):
        return self.likes.count()






    
