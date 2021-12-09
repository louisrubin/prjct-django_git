from django.urls import path

from . import views

app_name = "usuarios"

urlpatterns = [
    path('', views.usuarios, name='usuarios'),
    path("admin/listar/", views.ListarAdmin.as_view(), name="admin_listar"),
    path("admin/nuevo", views.Nuevo_only_Admin.as_view(), name="admin_nuevo"),
]
