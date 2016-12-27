from django.shortcuts import render_to_response
from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.utils import simplejson
from models import User
class UserForm(forms.Form): 
    '''
    username = forms.CharField(label='user',max_length=100)
    password = forms.CharField(label='pass',widget=forms.PasswordInput())
    '''
    username = forms.CharField()
    password = forms.CharField()   
    
    
def login(request):
    print request
    uf = UserForm(request.POST)
    if uf.is_valid():
        username=uf.cleaned_data['username']
        password=uf.cleaned_data['password']
        User.objects.create(username=username,password=password)
        response=HttpResponse("sdfsfsdf")
        response.set_cookie('uername',username,3600)
        return response
        

    
    
    

def index(request):    
    return render_to_response('index.html',context_instance=RequestContext(request)) 