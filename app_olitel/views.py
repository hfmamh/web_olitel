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
    return render(request, "form_star.html", context)

from .models import productos

def vista_tabla(request):
    #context ={}
    query_results = productos.objects.all()
    #context['tabla']=query_results
    return render(request, "tabla.html", locals())

from django.forms import formset_factory
def formset_vista(request):
    context={}
    app_formset=formset_factory(WidgetForm_ejemplo, extra=5)
    formset=app_formset()
    context['formset']= formset
    return render(request, "home_formset.html", context)



from django.http import JsonResponse
from .models import cotizaciones

def guardar_cotizacion(request):
    if request.method == "POST":
        cotizacion = request.POST.get("cotizacion")
        codigo = request.POST.get("codigo")
        descripcion = request.POST.get("descripcion")
        nueva_cotizacion = cotizaciones.objects.create(cotizacion=cotizacion,
                                                       codigo=codigo,
                                                       descripcion=descripcion)
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False})

from .models import cotizaciones

def obtener_cotizacion(request,cot_id):
    try:
        cotizacion = cotizaciones.objects.get(id=cot_id)  # Filtra la cotización por el identificador
        data = cotizacion.cotizacion
        return JsonResponse(data, safe=False)
    except cotizaciones.DoesNotExist:
        return JsonResponse({"error": "La cotización no existe"}, status=404)
    

def cotizaciones_vista(request):
    #context ={}
    query_results = cotizaciones.objects.all()
    #context['tabla']=query_results
    return render(request, "tabla_cotizaciones.html", locals())