from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from Final.models import Aceite,Comment, Avatar
from Final.forms import UserRegisterForm, AceiteForm, CommentForm, UserEditForm, AvatarFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User


def acerca_de_mi(request):
    return render(request, 'Final/about.html')

 
@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'Final/inicio.html')
    else:
        miFormulario = AvatarFormulario()
    return render(request, 'Final/agregarAvatar.html', {'miFormulario': miFormulario})  


def inicio(request):
    url = None
    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user.id)
        if avatares:
            url = avatares[0].imagen.url
    return render(request, 'Final/inicio.html', {'url': url})


def pepito(request):
    return  render(request, 'Final/pepito.html')


#def agregar_aceite(request):
 #   if request.method == 'POST':
  #      form = AceiteForm(request.POST)
   #     if form.is_valid():
    #        form.save()
     #       return redirect('Inicio')  # Redirigir a la lista de aceites después de guardar
    #else:
     #   form = AceiteForm()
    #return render(request, 'Final/agregar_aceite.html', {'form': form})

class AceiteCreate(CreateView):
    model = Aceite
    template_name = 'Final/agregar_aceite.html'
    form_class = AceiteForm  
    success_url = reverse_lazy('List')

class AceiteList(ListView):
     model= Aceite
     template_name = 'Final/lista_aceites.html'


class AceiteDetalle(DetailView):
     model= Aceite
     template_name = 'Final/detalle_aceite.html'


class AceiteActualizar(UpdateView):
    model=Aceite
    form_class = AceiteForm
    success_url = reverse_lazy('List')
    template_name = 'Final/actualizar_aceite.html'  
      


class AceiteDelete(DeleteView):
    model = Aceite
    success_url = reverse_lazy('List')
    template_name = 'Final/aceite_confirm_delete.html'


class CommentListView(ListView):
    model = Comment
    template_name = 'Final/comment_list.html'
    context_object_name = 'comments'

# View para agregar un nuevo comentario
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'Final/comment_form.html'
    success_url = reverse_lazy('comment_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    @method_decorator(login_required(login_url='Login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'Final/comment_edit.html'  
    success_url = reverse_lazy('comment_list')


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'Final/comment_confirm_delete.html'
    success_url = reverse_lazy('comment_list')

class CommentDetailView(DetailView):
    model = Comment
    template_name = 'Final/comment_detail.html'
    context_object_name = 'comment'








def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "Final/inicio.html")
            else:
                return render(request, "Final/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "Final/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "Final/login.html", {"form": form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "Final/inicio.html", {"mensaje": f"Usuario '{username}' creado exitosamente."})
    else:
        form = UserRegisterForm()

    return render(request, "Final/register.html", {"form": form})

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "Final/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "Final/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

