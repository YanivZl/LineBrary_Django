"""LineBrary_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Books import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("" , views.homepage , name="homepage"),
    path("login/" , views.login_page , name="login_page"),
    path("register/" , views.register , name="register"),
    path("logout/" , views.logout_user , name="logout_user"),
    path("addbook/" , views.add_book , name="add_book"),
    path("user/", views.user, name="user"),
    path("linkBooks", views.linkBooks, name="link_books"),
    #path("booksInStation", views.bookLocation, name="book_location"),
    path("selecrRoute" , views.SelectRoute , name="selectRoute")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
