from django.test import TestCase
from .models import Profile,Image,Comments
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTEst(TestCase):
    def setUp(Self):
        '''
        Set up class to create a new profile
        '''
        self.mercy = User(username = 'Mercy',email = 'mercy@gmail.com')
        self.mercy = Profile(user = Self.mercy,user_id = 1,bio = 'Love instagram',profile_pic = 'pic.jpg')

    def test_instance(self):
        '''
        Test class to test instantiation
        '''
        self.assertTrue(isinstance(self.mercy,Profile))

    def test_save_profile(self):
        '''
        Test to test if a profile is saved
        '''
        self.save_profile()
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        '''
        Test to see if a profile can be deleted 
        '''
        self.mercy.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)

class ImageTestCase(TestCase):
    def setUp(self):
        '''
        Creating new instances of the image
        '''
        self.new_post = Image(ig_pic = 'pic.jpg',name = 'picture',caption = 'Nice picture',user = mercy,likes = 0)


    def test_save_image(self):
        '''
        Test case to save image post created
        '''
        self.picture.save_image()
        pictures = Image.objects.all()
        self.assertEqual(len(pictures),1)

    def test_delete_image(self):
        '''
        Test case to test the deletion of an image
        '''
        self.picture.save_image()
        self.picture.delete_image()
        picture_list = Image.objects.all()
        self.assertTrue(len(image)==0)

    def test_get_all_images(self):
        '''
        Test case to get all images posted
        '''
        self.picture.save_image()
        all_pictures = Image.get_all_images()
        self.assertTrue(len(all_pictures) < 1)

    def test_get_one_image(self):
        '''
        Test to get one image post
        '''
        self.food.save_image()
        one_pic = Image.get_one_image(self.food.id)
        self.assertTrue(one_pic.name == self.picture.name)

class CommentTestCase(TestCase):
    def setUp(self):
        self.comment=Comment(body="So Nice",image_id=self.bmw.id,user = self.mercy')    

        

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    def test_save_comment(self):
        '''
        Test case to save comments on posts
        '''
        self.comment.save_comment()
        comments = Comments.objects.all()
        self.assertEqual(len(comments),1)

    def test_delete_comment(self):
        '''
        Test case to test the deletion of a comment
        '''
        self.comment.save_comment()
        self.comment.delete_comment()
        comment_list = Comments.objects.all()
        self.assertTrue(len(comment_list)==0)

