from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
 
 
def index(request):
  return HttpResponse("Hello Geeks")

from .forms import InputForm_ejemplo
 
# Create your views here.
def formulario_nombre(request):
    context ={}
    context['form']= InputForm_ejemplo()
    return render(request, "home_2.html", context)