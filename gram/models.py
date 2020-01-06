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
        '''
        Function for searching a user
        '''
        found_user = User.objects.get(username = username)

    def save_profile(self):
        '''
        Function for saving a profile
        '''
        self.save()

    def delete_profile(self):
        '''
        Function for deleting aprofile
        '''
        self.delete()

class Image(models.Model):
    ig_pic = models.ImageField(upload_to= 'pictures/')
    name = models.CharField(max_length=50)
    caption = models.CharField(max_length=300)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes' ,blank=True,)
    

    def save_image(self):
        '''
        Function for saving an image
        '''
        self.save()

    def delete_image(self):
        '''
        Function for deleting an image
        '''
        self.delete()

    @classmethod
    def all_images(cls):
        '''
        Function for getting all images posted
        '''
        timeline_pics = cls.objects.all()
        return timeline_pics

    @classmethod
    def user_pics(cls,user):
        '''
        Function for getting posts by a certain user.
        Args:user, the user who posted the image
        '''
        user_pic = cls.objects.filter(user = user)
        return user_pic

    @classmethod
    def one_pic(cls,id):
        '''
        Function for getting a single post
        Args:id The id of the post
        '''
        one_pic = cls.objects.filter(id = id)
        return one_pic

    
    @classmethod
    def search_image(cls,search_term):
        '''
        Function for searching image by name
        Args:serch_term,The entered keyword to be searched
        '''
        searched_image = cls.objects.filter(name =search_term)
        return searched_image


    @property
    def all_likes(self):
        '''
        Function for getting all likes
        '''
        return self.likes.count()


class Comments(models.Model):
    ig_pic_id = models.ForeignKey(Image,on_delete=models.CASCADE)
    text = models.CharField(max_length=1500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    @classmethod
    def get_all_comments(cls,id):
        '''
        Function for geting all comments
        '''
        comments = cls.objects.filter(ig_pic_id=id)
        return comments

    def save_comments(self):
        '''
        Function for saving posted comments
        '''
        self.save()

    def delete_comment(self):
        '''
        Function for deleting a comment
        '''
        self.delete()






    
