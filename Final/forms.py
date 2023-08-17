from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Final.models import Aceite, Comment, Avatar


class Productos(forms.Form):
    art = forms.IntegerField()
    nombre = forms.CharField()
    uso = forms.CharField()

class AceiteForm(forms.ModelForm):
    class Meta:
        model = Aceite
        fields = ['nombre', 'descripcion', 'uso', 'imagen']

    # Personaliza el aspecto de los campos del formulario si es necesario
    widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'uso': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Uso'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }

class Accesorios(forms.Form):
    art = forms.IntegerField()
    nombre = forms.CharField()
    uso = forms.CharField()

class AromaTerapia(forms.Form):
    art = forms.IntegerField()
    nombre = forms.CharField()
    uso = forms.CharField() 

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}       


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
class UserEditForm(UserCreationForm):

    
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']




class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']