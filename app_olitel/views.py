from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
def index(request):
  return HttpResponse("Hello Geeks")

from .forms import InputForm_ejemplo
def formulario_nombre(request):
    context ={}
    context['form']= InputForm_ejemplo()
    return render(request, "home_2.html", context)

def formulario_3(request):
    print(request.GET) 
    return render(request, "form_GET.html")

def formulario_4(request):
    print(request.POST) 
    return render(request, "form_POST.html")

from .forms import WidgetForm_ejemplo
def form_widgets(request):
    context = {}
    form = WidgetForm_ejemplo(request.POST or None)
    context['form'] = form
    return render(request, "home.html", context)