from django.db import models



# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='pictures/')
    bio = models.CharField(max_length=300)
    username = models.CharField(max_length=50,default='Your username')

    def __str__(self):
        return self.username

class Image(models.Model):
    ig_pic = models.ImageField(upload_to= 'pictures/')
    name = models.CharField(max_length=50)
    caption = models.CharField(max_length=300)
    user = models.ForeignKey(Profile,on_delete = models.CASCADE)
    

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



    
