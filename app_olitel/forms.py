from django import forms
   
# creating a form 
class InputForm_ejemplo(forms.Form):
   
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(
                     help_text = "Enter 6 digit roll number"
                     )
    password = forms.CharField(widget = forms.PasswordInput())

class WidgetForm_ejemplo(forms.Form):
    title = forms.CharField(widget = forms.Textarea)
    description = forms.CharField(widget = forms.CheckboxInput)
    views = forms.IntegerField(widget = forms.TextInput)
    available = forms.BooleanField(widget = forms.Textarea)
    date = forms.DateField(widget = forms.SelectDateWidget)

from .models import modelo_1
class form_model(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = modelo_1
        fields = "__all__"

from .models import productos
class form_producto(forms.ModelForm):
    class Meta:
        model = productos
        fields = "__all__"

