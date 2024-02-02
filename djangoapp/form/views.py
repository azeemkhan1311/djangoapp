from django.shortcuts import render
from datetime import datetime
import os
import json

# Create your views here.
def index(request):
    return render(request, 'home.html')

def currentDate():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def home_view(request):
    our_date = currentDate()
    return render(request, 'home.html', {'our_date': our_date})

def form_view(request):
    if request.method == 'POST':

        # Getting the submitted data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        current_directory = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(current_directory, './templates/data.json')


        with open(json_file_path) as json_file:
            users = json.load(json_file)
            users.append({'name': name, 'email': email, 'phone': phone})
            
            # writing json file
            with open(json_file_path, 'w') as json_file:
                json.dump(users, json_file, indent=2)

    return render(request, 'form.html')
