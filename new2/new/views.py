from django.shortcuts import render
from django.http import HttpResponse

 # Create your views here.

def index(request):
     return render(render,"hello\index.html")
def greet(request,name):
     return HttpResponse(f"hello {name}, hafa")
# Create your views here.
