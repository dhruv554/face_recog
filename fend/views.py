from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import People_Details, SearchImages
import os

# Create your views here.

def home(request):    
    return render(request, "home.html")


def signup(request):

        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            password = request.POST['password']
            password2 = request.POST['password2']
            email = request.POST['email']

            if password == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username is already taken!!')
                    return redirect('signup')

                elif User.objects.filter(email=email).exists(): 
                    messages.info(request,'Email is already taken!!')
                    return redirect('signup')

                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    print('User Created')
                    return redirect('signin')

            else:
                messages.info(request,'Password not Matching..!!')
                return redirect('signup')

        else:
            return render(request, "signup.html")


def signin(request):

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('/')
            
            else:
                messages.info(request,'Invalid Credentials..!!')
                return redirect('signin')

        else:
            return render(request, "signin.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def regdetail(request):

    if request.method == 'POST':

        reg = People_Details()
        reg.name = request.POST['name']
        reg.age = request.POST['age']
        reg.gender = request.POST['gender']
        reg.phone = request.POST['phone']
        reg.county = request.POST['county']
        reg.image = request.FILES['image']

        reg.save()
        return redirect('/')

    else:
        return render(request,'regdetail.html')
        

def runsearch(request):

    if request.method == 'POST':

        simg = SearchImages()
        simg.image = request.FILES['image']
        
        url=simg.image.name
        os.system("python recognize_faces_image.py --encodings encodings.pickle --image test/"+url+" --detection-method hog")
        print(url)

        simg.save()
        return redirect('/')

    else:
        return render(request,'runsearch.html')