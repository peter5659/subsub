from django.shortcuts import render

# Create your views here.
def signIn(request) :
    return render(request, 'signin.html')

def signUp(request) :
    return render(request, 'signup.html')

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