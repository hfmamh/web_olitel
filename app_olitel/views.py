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

from .forms import form_model
def form_modelo(request):
    context ={}
 
    # create object of form
    form = form_model(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
    context['form']= form
    return render(request, "home.html", context)

from .forms import form_producto
def crear_producto(request):
    context ={}
    form = form_producto(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form']= form
    return render(request, "home.html", context)
