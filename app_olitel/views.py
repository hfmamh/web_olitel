from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
 
 
def index(request):
  return HttpResponse("Hello Geeks")

from .forms import InputForm
 
# Create your views here.
def home_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "home.html", context)