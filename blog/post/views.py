from django.shortcuts import render, HttpResponse
from django.template.context_processors import request
from post import models
# Create your views here.
user_list=[
    {"user":"jack","pwd":"abc"},
    {"user":"tom","pwd":"ABC"},]


def index(request):
    if request.method == 'POST':
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        #cong
        models.UserInfo.objects.create(user = username , pwd = password)
        
        user_list = models.UserInfo.objects.all()
        
        print(username,password)
    return render(request, 'index.html',{"data":user_list})