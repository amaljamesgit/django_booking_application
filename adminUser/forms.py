from django.forms import ModelForm
from django import forms
#from adminUser.models import *
from django.contrib.auth.models import User

 
# define the class of a form
class UserForm(ModelForm):
    class Meta:
        # write the name of models for which the form is made
        model = User       
 
        # Custom fields
        fields =["username", "password"]
 
    # this function will be used for the validation
    def clean(self):
 
        # data from the form is fetched using super function
        super(User, self).clean()
         
        # extract the username and text field from the data
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
 
        # conditions to be met for the username length
        # if len(username) < 5:
        #     self._errors['username'] = self.error_class([
        #         'Minimum 5 characters required'])
        # if len(text) <10:
        #     self._errors['text'] = self.error_class([
        #         'Post Should Contain a minimum of 10 characters'])
 
        # return any errors if found
        return self.cleaned_data