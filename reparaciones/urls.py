from django.urls import path
from .views import login_view, pagina_principal_usuario, pagina_principal_tecnico, logout_view
from reparaciones import views

urlpatterns = [
    path('', login_view, name='login'),
    path('inicio/', views.inicio, name="inicio"),
    path('pagina_principal_usuario/', views.pagina_principal_usuario, name='pagina_principal_usuario'),
    path('pagina_principal_tecnico/', views.pagina_principal_tecnico, name='pagina_principal_tecnico'),
    path('logout/', logout_view, name='logout'),
    # Agrega otras URL según sea necesario
]
