from django.urls import path
from Final import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from  django.conf.urls.static import static

urlpatterns = [
    path('',views.inicio, name='Inicio'),
    path('about', views.acerca_de_mi, name='About'),
    path('pepito',views.pepito,name='Pepito'),
    path('list', views.AceiteList.as_view(), name='List'),

    
    path('aceite/<int:pk>', views.AceiteDetalle.as_view(), name='Detail'),

    
    path('nuevo', views.AceiteCreate.as_view(), name='New'),
    
    
    
    path('editar/<int:pk>', views.AceiteActualizar.as_view(), name ='Edit'),

    
    path('borrar/<int:pk>', views.AceiteDelete.as_view(), name='Delete'),
    path('login/', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='Final/logout.html'), name = 'Logout'),
    
    path('comments/', views.CommentListView.as_view(), name='comment_list'),
    path('comments/add/', views.CommentCreateView.as_view(), name='comment_add'),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment_detail'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
    path('agregarAvatar', views.agregarAvatar, name='AgregarAvatar'),
    
    ]



