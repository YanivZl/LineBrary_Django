from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import User , Book , BookStationRelation , Order , categories, Contributions, Wishlist, stations , Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import BookForm, BookStationRelationForm , ProfileForm , RouteForm
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from random import shuffle
import os
import json
# Create your views here.


def homepage(request):
    if request.user.is_authenticated:
        user = Profile.objects.filter(user= request.user)
        user_name_and_last = user[0].first_name + ' ' +  user[0].last_name
        Books_For_Recomended = Book.objects.all().order_by('?')[:20]
        categories_array = [tup[0] for tup in categories]
        shuffle(categories_array)
        categories_books_relation_array = {}
        booksInStation = list(BookStationRelation.objects.filter(station=user[0].default_station).values_list('book', flat=True))
        for category in categories_array:
            booksInCategory = Book.objects.filter(ISBN13__in=booksInStation).filter(gener=category)
            
            if len(booksInCategory) > 0:
                categories_books_relation_array[category] = booksInCategory
        return render(request , "Books/index.html", { 'User_Name' : user_name_and_last , 'Books_For_Recomended' : Books_For_Recomended , 'categories' : categories_array , 'books' : categories_books_relation_array })
    else: 
        return redirect("login_page")

def login_page(request): 
    if request.method == 'GET':   
        return render(request , "Books/login.html", {'login_form' : AuthenticationForm()})
    else:
        user = authenticate(request, username= request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'Books/login.html', { 'login_form': AuthenticationForm() , 'errMsg' : 'User is not exsists, or password is incorrect'})
        else:
            login(request, user)
            return redirect('homepage')

def register(request):
    if request.method == 'GET':
        return render(request, 'Books/register.html', {'user_form': UserCreationForm() , 'profile_form' : ProfileForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:    
                user = User.objects.create_user(username= request.POST['username'], password=request.POST['password1'])
                profile = Profile(user=user , first_name= request.POST['first_name'] , last_name= request.POST['last_name'] , email=request.POST['email'] , default_station=request.POST['default_station'])
                user.save() 
                profile.save()
                login(request, user)
                return redirect('homepage')
            except IntegrityError:
                return render(request, 'Books/register.html', {'user_form': UserCreationForm(),  'profile_form' : ProfileForm(),
                                                                     "errMsg": "User exists. Choose a different one"})
        else:
            return render(request, 'Books/register.html', {'user_form': UserCreationForm(), 'profile_form' : ProfileForm(),
                                                                 "errMsg": "Password didn't match"})


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login_page')

def add_book(request):
    if request.method == 'GET':
        return render(request, 'Books/addbook.html', {'station_form' : BookStationRelationForm() , 'book_form' : BookForm() })
    else:
        if request.POST['bookname'] != "" and request.POST['author'] != "" and request.POST['description'] != "" and request.POST['language'] != "" and request.POST['page_count'] != 0:
            b = Book(ISBN13=random.randint(0 , 999999999)  , bookname= request.POST['bookname'] , author= request.POST['author'] , gener= request.POST['gener'] , page_count= request.POST['page_count'] , condition=request.POST['condition'], image=request.POST['image'], language= request.POST['language'], description= request.POST['description'] , cover_type= request.POST['cover_type'])
            b.imageURL = 'Books/Images/' +  b.image.url
            b.save()
            bsr = BookStationRelation(station=request.POST["station"], book= b)
            bsr.save()
            return redirect('homepage')
        else:
            return render(request, 'Books/addbook.html', {'station_form' : BookStationRelationForm() , 'book_form' : BookForm() , 'errMsg' : "An error occurred. The book isn't uploaded. Plese check the correctness." })

def user(request):
    if request.method == 'GET':
        orders = Order.objects.filter(user__username=request.user)
        contributions= Contributions.objects.filter(user__username=request.user)
        wishlist= Wishlist.objects.filter(user__username=request.user)
        return render(request,'Books/user.html',{'User_Name':request.user, "orders" : orders, 'contributions':contributions,}  )

def loans(request):
    if request.method=='POST':
        user = request.user
        station=request.POST['station']
        book=request.POST['book'] 
        id=Order.objects.create(user=user,ISBN13=book, station=station )
        BookStationRelation.objects.filter(book=book, station=station).delete()
        return JsonResponse({})       

def linkBooks(request):
    if request.method == 'GET':
        BookStationRelation.objects.all().delete()
        books = Book.objects.all()
        for i in range(len(books)):
            r = BookStationRelation.objects.create(ISBN13=books[i], station=stations[i % len(stations)][0])
            r.save()
        return JsonResponse({})

def SelectRoute(request):
    if request.method == 'GET':
        return render(request, 'Books/selectRoute.html', { 'route_form' : RouteForm()})
    else:
        stations_by_route = ['Tel Aviv HaHagana' , 'Tel Aviv Ha Shalom' , 'Savidor-Center Tel Aviv' , 'Tel Aviv University' , 'Herzliya' ,'Haifa - Hof Hakarmel' , 'Haifa - Bat Galim' , 'Haifa - Merkaz Hashmuna' , 'Haifa - Merkazit HaMifrats' , 'Haifa - Hutsot HaMifrats']
        start = request.POST['starting_station']
        end = request.POST['dest_station']
        start_to_end = [ station for station in stations_by_route]
        availible_stations = []
        if  stations_by_route.index(start_to_end[0]) < stations_by_route.index(start_to_end[len(stations_by_route) - 1]):
            for station in stations_by_route:
                availible_stations.append(BookStationRelation.objects.all().filter(station=station).filter(book=Books.objects.all().filter(bookname=request.POST['select_book'])))
        return render(request , 'Books/selectRoute.html', {'route_form' : RouteForm() , 'book' : request.POST['select_book'] , 'stations' : availible_stations})

def books_search(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        books = Book.objects.filter(bookname__contains=name)
        res = json.loads(serializers.serialize('json', books))
        return JsonResponse(res, safe=False)

def  bookByStation(request):
    if request.method =='GET':
        name=request.GET.get('name')
        station=BookStationRelation.objects.filter(book__bookname=name)
        res= json.loads(serializers.serialize('json', station))
        return JsonResponse(res, safe=False)
