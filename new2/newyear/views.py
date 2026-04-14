from django.shortcuts import render
import datetime

now = datetime.datetime.now()
def new(request):
    return render(request,"newyear\index.html",{
        "newyear" : now.day==1 and now.month==1
    })

# Create your views here.
 