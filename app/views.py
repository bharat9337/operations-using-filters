from django.shortcuts import render

# Create your views here.


def userfilters(request):
    d={'data':'East or west HARSHAD is best'}
    return render(request,'userfilters.html',d)