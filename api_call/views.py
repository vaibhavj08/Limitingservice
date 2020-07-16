from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from django.contrib import auth
from django.contrib.auth.models import User


# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username = username,password = password)
        user.save()
        return redirect('/')
    else:
        return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username =username,password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/api_call')
        else:
            return HttpResponse("<h1>403 Forbidden</h1>")
    else:
        return render(request,'login.html')


one_minute = 60
count = 0
hour_request_count=300


def api_call(request):
    global count

    url = 'http://127.0.0.1:8000/get_number'
    try:
        response = requests.get(url,timeout=2)
        count = count+1
        print('count:',count)

    except requests.exceptions.ReadTimeout:
        return render(request,'api.html',{'response':'403 Forbidden'})

    return render(request,'api.html',{'response':response.text})


def remaining_call(request):
    r_call = hour_request_count-count
    return HttpResponse(r_call)