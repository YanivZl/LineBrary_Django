from django.core.management.base import BaseCommand
import json
import os
from pathlib import Path
from Books.models import Book

fathfath_dir = os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir)))
fathfath_dir = os.path.dirname(os.path.abspath(os.path.join(fathfath_dir , os.pardir)))
json_dir = os.path.join(fathfath_dir, 'static' , 'Books' , 'books.json')




class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open(json_dir) as books_json:
            books = json.load(books_json)
        for book in books:
            if 'isbn' in book.keys() and 'title' in book.keys() and 'pageCount' in book.keys() and 'thumbnailUrl' in book.keys() and 'shortDescription' in book.keys() and 'authors' in book.keys() and 'categories' in book.keys() and len(book['categories']) > 0:
                b = Book(ISBN13= book['isbn'] , bookname= book['title'] , author= book['authors'][0], gener= book['categories'][0] , page_count= int(book['pageCount']) , condition='Like New', imageURL= book['thumbnailUrl'] , language= 'English', description= book['shortDescription'] , cover_type= 'Soft')
                b.save()
                