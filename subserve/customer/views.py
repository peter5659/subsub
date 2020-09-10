from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Customer
from django.http import HttpResponse
# Create your views here.
def signUp(request) :
    if request.method=="POST":
        if request.POST['password']==request.POST['passwordCheck']:

            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'signup.html',{'error':"Username has already been taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password'], email = request.POST['email'])
                name = request.POST['name']
                if request.POST['sex']=="male":
                    sex = 1
                else:
                    sex = 0
                address = request.POST['address']
                birthday = request.POST['birthday']
                phone = request.POST['phone']
                customer = Customer(name= name, address = address, birthday = birthday, phone = phone, sex = sex, user= user)
                customer.save()
                auth.login(request, user)
                return HttpResponse("Signned up!!")
        else:
            return render(request, 'signup.html', {'error': "Password doesn't match"})
    else:
        return render(request, 'signup.html')
def signIn(request) :
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        customer = auth.authenticate(request, username = username, password = password)
        if customer is not None:
            auth.login(request,customer)
            print(customer.username)
            return redirect("/")
        else:
            return render(request, 'signin.html', {'error': "There is No user"})
    else:
        return render(request, 'signin.html')



def myPage(request) :
    return render(request, 'mypage.html')

def editProfile(request) :
    return render(request, 'editprofile.html')

def findAccount(request) :
    return render(request, 'findaccount.html')

def confirmPassword(request) :
    return render(request, 'confirmpassword.html')

def resign(request) :
    return render(request, 'resign.html')