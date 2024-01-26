from django.http import HttpResponse
from django.shortcuts import render

data = {
  'movies':[

    { 'id':75,
     'name' :"good_man",
     'release' : 2004
    },
     {'id':86,
     'name' :"bat_man",
     'release' : 2000
    },
     { 'id':75,
     'name' :"wonder_man",
     'release' : 2002
    }

    ]
}

def authenticationproj(request):
  return render(request,'templates/authenticationproj/home.html',data)

def home(request):
  return HttpResponse("welocome")