from django.test import TestCase
from .models import Image, Comment, Profile, Follow
from django.contrib.auth.models import User

class ImageTestClass(TestCase):
    def setUp(self):
        self.wenslaus = User(username = "wenslaus", email = "wenslaus@gmail.com",password = "1234")
        self.profile = Profile(bio='bio', user= self.wenslaus)
        self.food = Image(image = 'imageurl', name ='food', caption = 'Chicken Taco', profile = self.profile)
        self.maua = Image(image = 'imageurl', name ='maua', caption = 'Lillies', profile = self.profile)

        self.wenslaus.save()
        self.profile.save()
        self.food.save_image()

    def tearDown(self):
        Image.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.food, Image))

    def test_save_image_method(self):
        images = Image.objects.all()
        self.assertTrue(len(images)> 0)

    def test_delete_image(self):
        images1 = Image.objects.all()
        self.assertEqual(len(images1),1)
        self.food.delete_image()
        images2 = Image.objects.all()
        self.assertEqual(len(images2),0)

    def test_update_caption(self):
        self.food.update_caption('Italian')
        self.assertEqual(self.food.caption, 'Italian')

    def test_get_profile_images(self):
        self.maua.save_image()
        images = Image.get_profile_images(self.profile)
        self.assertEqual(len(images),2)

class ProfileTestClass(TestCase):
    def setUp(self):
        self.wenslaus = User(username = "wenslaus", email = "wenslaus@gmail.com",password = "1234")
        self.profile = Profile(bio='bio', user= self.wenslaus)
        self.wenslaus.save()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.wenslaus, User))
        self.assertTrue(isinstance(self.profile, Profile))

    def test_search_user(self):
        user = Profile.search_user(self.wenslaus)
        self.assertEqual(len(user), 1)

class CommentTestClass(TestCase):
    def setUp(self):
        self.wenslaus = User(username = "wenslaus", email = "wenslaus@gmail.com",password = "1234")
        self.profile = Profile(bio='bio', user= self.wenslaus)
        self.food = Image(image = 'imageurl', name ='food', caption = 'Chicken Taco', profile = self.profile)
        self.comment = Comment(image=self.food, content= 'Looks delicious', user = self.wenslaus)

        self.wenslaus.save()
        self.profile.save()
        self.food.save_image()
        self.comment.save_comment()

    def tearDown(self):
        Image.objects.all().delete()
        Comment.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment(self):
        comments = Comment.objects.all()
        self.assertTrue(len(comments)> 0)

    def test_delete_comment(self):
        comments1 = Comment.objects.all()
        self.assertEqual(len(comments1),1)
        self.comment.delete_comment()
        comments2 = Comment.objects.all()
        self.assertEqual(len(comments2),0)

    def test_get_image_comments(self):
        comments = Comment.get_image_comments(self.food)
        self.assertEqual(comments[0].content, 'Looks delicious')
        self.assertTrue(len(comments) > 0)

class FollowTestClass(TestCase):
    def setUp(self):
        self.wenslaus = User(username = "wenslaus", email = "wenslaus@gmail.com",password = "moringa")
        self.profile1 = Profile(bio='bio', user= self.wenslaus)        
        self.tony = User(username = "tony", email = "tony@gmail.com",password = "moringa")
        self.profile2 = Profile(bio='bio', user= self.tony) 
        self.wenslaus.save()
        self.tony.save()
        self.follow = Follow (followed = self.profile1, follower = self.profile2 )
        
    def tearDown(self):
        Profile.objects.all().delete()        
        User.objects.all().delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.follow,Follow))