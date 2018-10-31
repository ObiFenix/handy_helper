# Imported Modules and Classes from User Models
# =============================================

# from django.shortcuts import render, HttpResponse, redirect
# from datetime import datetime
# from .models import *
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from .models import User
import bcrypt


# Required Custom views
# =====================

# < Home Page Registration: '/' >
def homeView(request):
    if 'uid' in request.session: return redirect('/handyhelper')
    request.session['status'] = 'Register'
    return redirect('/login')

# < Home Page Registration: '/' >
def registerView(request):
    if 'uid' in request.session: return redirect('/handyhelper')
    request.session['status'] = 'Register'
    return render(request,'Register.html')

# < Home Page Login: '/login/' >
# < Unbrela to Switch between Login and Register views/pages >
def loginView(request):
    if 'uid' in request.session:
        return redirect('/handyhelper')
    request.session['status'] = 'Login'
    return render(request, 'Login.html')

# < Successfly Logged out -> redirect to Home Pge >
def logoutView(request):
    request.session.flush()
    return redirect('/login')

# < Required Login Page >
# ======================>
    # If there are errors, they will display as dismissable alerts
    # on the homepage, otherwise it will proceed and login in the user
def loginUserForm(request):
    errors = User.objects.loginValitator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
    else:
        try:
            user = User.objects.get(email=request.POST['login_email'])
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['first_name'] = user.first_name
                request.session['uid']        = user.id
                return redirect('/handyhelper')
        except User.DoesNotExist:
            pass
        messages.error(request, 'Login unsuccessful! Please check your email and passowrd!', extra_tags='dontExist')
    return redirect('/login')

# < Registration Login Page >
def registerUserForm(request):
    errors = User.objects.registerValitator(request.POST)
    pwHash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
            # return redirect('/handyhelper')
    else:
        try:
            # Create New User
            user = User.objects.create(
                first_name = request.POST['first_name'],
                last_name  = request.POST['last_name'],
                email      = request.POST['email'],
                password   = pwHash)
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            request.session['uid'] = user.id
            return redirect('/handyhelper')
        except IntegrityError:
            messages.error(request, 'This email already exists!', extra_tags='email')
        # return redirect('/')
    return redirect('/register')
