from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date, timezone
# Create your models here.





categories = [ ('Open Source' , 'Open Source' ), ('Mobile' , 'Mobile'), ('Java' , 'Java') , ('Software Engineering' , 'Software Engineering'), ( 'Internet' , 'Internet') ,( 'Web Development' , 'Web Development') ,( 'Miscellaneous' , 'Miscellaneous') , ('Microsoft .NET' , 'Microsoft .NET') , ('Object-Oriented Programming' ,  'Object-Oriented Programming' ), ( 'Networking' , 'Networking' ) ,('Theory', 'Theory') , ('Programming', 'Programming') , ('Python', 'Python') , ('PowerBuilder' , 'PowerBuilder' ) , ('Computer Graphics' , 'Computer Graphics' ) , ( 'Mobile Technology' , 'Mobile Technology' ) , ('Business' , 'Business' ) , ('Microsoft' , 'Microsoft') , ('P' , 'P') , ('XML' , 'XML') , ('Perl' , 'Perl') , ('Client-Server' , 'Client-Server')]

stations_temp = [
    'Tel Aviv - Savidor Center',
    'Tel Aviv - University',
    'Tel Aviv - Ha-Shalom',
    'Tel Aviv - Ha-Hagana',
    'Haifa - Merkazit HaMifrats',
    'Haifa - Merkaz Hashmuna',
    'Haifa - Bat Galim',
    'Haifa - Hof Hakarmel',
    'Netanya',
    'Herzliya',
]

stations = []

for s in stations_temp:
    new_tup = (s , s)
    stations.append(new_tup)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    default_station = models.CharField(max_length=100,choices=stations , default='Tel Aviv - Savidor Center')

class Book(models.Model):
    ISBN13 = models.CharField(max_length=13 , primary_key=True)
    bookname = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    gener = models.CharField(max_length=100 , choices=categories , default="")
    page_count = models.IntegerField(null=True)  
    condition = models.CharField( max_length = 20 ,choices=[('Like New' ,'Like New'), ( 'Used' ,'Used'), ( 'Collectible' , 'Collectible')], default='LikeNew')
    image = models.ImageField(upload_to='Books/Images/')
    imageURL = models.URLField(blank=True)
    language = models.CharField(max_length=20)
    description = models.CharField(max_length=2000 , default="")
    cover_type = models.CharField(max_length = 20 , choices=[( 'Hard' ,'Hard'), ( 'Soft' , 'Soft')], default='Hard')


class BookStationRelation(models.Model):
    book = models.ForeignKey(Book , on_delete=models.CASCADE)
    station = models.CharField(max_length=100 , choices=stations , default='Tel Aviv - Savidor Center')

class Order(models.Model):
    user = models.ForeignKey(Profile , on_delete=models.CASCADE)
    ISBN13 = models.ForeignKey(Book , on_delete=models.CASCADE)
    station = models.CharField(max_length=100 , choices=stations , default='Tel Aviv - Savidor Center')

class Contributions(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    ISBN13 = models.ForeignKey(Book , on_delete=models.CASCADE)
    station = models.CharField(max_length=100 , choices=stations , default='Tel Aviv - Savidor Center')
    condition = models.CharField( max_length = 20 ,choices=[('Like New' ,'Like New'), ( 'Used' ,'Used'), ( 'Collectible' , 'Collectible')], default='LikeNew')


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ISBN13 = models.ForeignKey(Book , on_delete=models.CASCADE)
