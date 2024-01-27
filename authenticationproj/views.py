from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import Movie

def home(request):
  return HttpResponse("welocome")



def authenticationproj(request):
  data=Movie.objects.all() #  will generate a query to get all the data from the detabase 
  return render(request,'authenticationproj/home.html',{'movies':data})


def add(request):
  #getting data from the browser ussing http post method
  title = request.POST.get('title')
  year = request.POST.get('year')
  #if the user had entered any data it shoud be added in the db and then rendered
  if title and year :
    #create an obj of class Movie and then send it to be rendered
    movie=Movie(title=title,year=year)
    movie.save()
    return HttpResponseRedirect('/authenticationproj') #this page appears after data is added
  return render(request,'authenticationproj/add.html')
