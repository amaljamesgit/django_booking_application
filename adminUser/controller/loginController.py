from django.shortcuts import *
from django.http import HttpResponse
from django.template import loader
from adminUser.forms import UserForm
from django.core.validators import *
from django.contrib.auth import *
from django.contrib.auth.models import User
import re

# Create your views here.

def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        error_msg = formValidation(request)
        if(error_msg != False):
            return render(request, 'auth/admin_login.html',{'error_msg' : error_msg,'email' : email,'password' : password})
       # return render(request, 'auth/admin_login.html')
        user = authenticate(
                    username=email,
                    password=password,
                )
        if user is not None:
            return redirect('dashboard')
        else:
            error_msg = {'error_message': "Incorrect username or password",'name' : 'login_error'}
            return render(request, 'auth/admin_login.html',{'error_msg' : error_msg,'email' : email,'password' : password})

    else:
        #form = UserForm(None)
        return render(request, 'auth/admin_login.html')
    

def formValidation(request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if  len(email) == 0:
            return {'error_message': "Enter Valid Mail",'name' : 'mail'}
        if re.fullmatch(regex, email):
            print('sssss');
        else:
            return {'error_message': "Enter Valid Mail",'name' : 'mail'} 
        if not password:
            error_message = 'Password is required'
            return {'error_message': "Enter Valid Password",'name' : 'password'}
        return False
        



       