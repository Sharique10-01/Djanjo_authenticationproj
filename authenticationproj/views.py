from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

def authenticationproj(request):
  return HttpResponse("welocome")

def home(request):
  data=Movie.objects.all() #  will generate a query to get all the data from the detabase 
  return render(request,'authenticationproj/home.html',{'movies':data})