from django.shortcuts import*
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect('login')

