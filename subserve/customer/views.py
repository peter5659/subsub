from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Customer
# Create your views here.
def signUp(request) :
    if request.method=="POST":
        if request.POST['password']==request.POST['passwordCheck']:
            name = request.POST['name']
            username = request.POST['username']
            if User.objects.get(username= username) is not None:
                return redirect("/")
            password = request.POST['password']
            passwordCheck = request.POST['passwordCheck']
            email = request.POST['email']
            if request.POST['sex']=="male":
                sex = 1
            else:
                sex = 0
            address = request.POST['address']
            birthday = request.POST['birthday']
            phone = request.POST['phone']
            user = User.objects.create_user(username = username, password = password, email = email)
            customer = Customer.objects.create(user=user, name= name, address = address, birthday = birthday, phone = phone, sex = sex)
            customer.save()
            print(customer.address)
            print(customer.sex)
            return redirect("/")
        else:
            return redirect("/")
    else:
        return render(request, 'signup.html')
def signIn(request) :
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request,user)
            print(user.username)
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