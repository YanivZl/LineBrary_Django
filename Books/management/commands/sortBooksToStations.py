from django.core.management.base import BaseCommand
from Books.models import BookStationRelation , Book

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        BookStationRelation.objects.all().delete()
        books = Book.objects.all()
        big_stations = ['Tel Aviv - Savidor Center' , 'Tel Aviv - University', 'Haifa - Hof Hakarmel']
        small_stations = ['Tel Aviv - Ha-Shalom','Tel Aviv - Ha-Hagana','Haifa - Merkazit HaMifrats', 'Haifa - Merkaz Hashmuna', 'Haifa - Bat Galim','Netanya', 'Herzliya']
        for station in big_stations:
            books = Book.objects.all().order_by('?')[:80]
            for book in books:
                bsr = BookStationRelation(station= station , book= book)
                bsr.save()
        for station in small_stations:
            books = Book.objects.all().order_by('?')[:20]
            for book in books:
                bsr = BookStationRelation(station= station , book= book)
                bsr.save()