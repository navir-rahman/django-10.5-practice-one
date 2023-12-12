from django.shortcuts import render
from datetime import datetime

current_datetime = datetime.now()
worddictionary = [
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
]
def home(request):
    return render(request, 'home.html', {"cd": current_datetime} )