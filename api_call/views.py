from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from django.contrib import auth
from django.contrib.auth.models import User


# Create your views here.
#function to signup
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username = username,password = password)
        user.save()
        return redirect('/')
    else:
        return render(request,'home.html')

#function to login
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username =username,password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/api_call')
        else:
            return HttpResponse("<h1>403 Forbidden</h1><h3>Wrong credential</h3>")
    else:
        return render(request,'login.html')


count = 0
hour_request_count=300

#function to call the api
def api_call(request):
    if request.user.is_anonymous:
        return redirect('/')
    global count

    url = 'http://127.0.0.1:8000/get_number'
    try:
        response = requests.get(url,timeout=2)
        count = count+1
        print('count:',count)

    except requests.exceptions.ReadTimeout:
        return render(request,'api.html',{'response':'403 Call limit exausted for a minute'})

    return render(request,'api.html',{'response':response.text})

#function to logout
def logout(request):
    auth.logout(request)
    return redirect('/')


#function to check the remaining calls in an hour
def remaining_call(request):
    r_call = hour_request_count-count
    return HttpResponse(r_call)