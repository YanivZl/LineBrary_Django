from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import BookStationRelation, Book, Order, Profile


stations = [
    'Tel Aviv - Savidor Center',
    'Tel Aviv - University',
    'Tel Aviv - Ha-Shalom',
    'Tel Aviv - Ha-Hagana',
    'Nahariya',
    'Akko',
    'Karmiel',
    'Ahihod',
    'Kiryat Motskin',
    'Kiryat Haim',
    'Haifa - Hutsot HaMifrats',
    'Haifa - Merkazit HaMifrats',
    'Haifa - Merkaz Hashmuna',
    'Haifa - Bat Galim',
    'Haifa - Hof Hakarmel',
    'Beit Sheaan',
    'Afula',
    'Migdal HaEmek',
    'Yofneaam',
    'Atlit',
    'Binayamina',
    'Keysaria - Pardes Hana',
    'Hedera West',
    'Netanya',
    'Netanya - Sapir',
    'Beit Yehushua',
    'Herzliya',
    'Petah Tikva - Kiryat Arye',
    'Petah Tikva - Sgula',
    'Rosh HaAin North',
    'Kfar Saba - Nordaoo',
    'Hod HaSharon - Sokolov',
    'Raanana South',
    'Airport Ben Gurion',
    "Modi'in outskirts",
    "Modi'in Center",
    'Jerusalem - Yizhak Navon',
    'Kfar Habad',
    'Lud - Ganei Aviv',
    'Lud/Ramla',
    'Beit Shemesh',
    'Jesrualem - Tanahi Zoo',
    'Jerusalem - Malha',
    'Mazkeret Batia',
    'Kiryat Malachi - Yoav',
    'Kiryat Gat',
    "Lehavim/Raha'at",
    "Be'er Sheva North - University",
    "Be'er Sheva Center",
    'Dimona',
    'Ofakim',
    'Netivot',
    'Sderot',
    'Ashkelon',
    'Asdod - Ad Halom',
    'Yavne - West',
    'Yavne - East',
    "Be'er Yakov",
    'Rishon Letsiyon - HaRishonim',
    'Rishon Letsiyon - Moshe Dayan',
    'Bat Yam - HaKomemiyut',
    'Bat Yam - Yoseftal',
    'Holon Junction'
]

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ('bookname', 'author', 'gener', 'language', 'page_count', 'condition', 'cover_type', 'image', 'description',)

class BookStationRelationForm(forms.ModelForm):

    class Meta:
        model = BookStationRelation
        fields = ('station',)

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'default_station',)


class RouteForm(forms.Form):
    choices = ('Savidor-Center Tel Aviv' , 'Tel Aviv University' , 'Tel Aviv Ha Shalom' , 'Tel Aviv HaHagana' , 'Haifa - Hutsot HaMifrats','Haifa - Merkazit HaMifrats','Haifa - Merkaz Hashmuna','Haifa - Bat Galim','Haifa - Hof Hakarmel')
    starting_station = forms.ChoiceField(choices=choices ,  label='Starting Station')
    dest_station = forms.ChoiceField(choices=choices , label='Destination Station')
