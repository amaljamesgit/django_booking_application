from django.urls import path

from . import views
from .controller import dashboradController,loginController

urlpatterns = [
    path('', dashboradController.index, name='index'),
    path('login', loginController.index, name='login'),
]