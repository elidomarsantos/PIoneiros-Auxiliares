from django.urls import path

from . import views



urlpatterns = [
    path('', views.home),
    path('publicadores/', views.publicadores),
    path('editar_lista/<int:id>', views.editar_lista),
    path('add_comissão/', views.add_comissão),
    path('editar_comissão/<int:id>', views.editar_comissão),
    path('deletar_publicador/<int:id>', views.deletar_publicador),
    path('deletar_comissão/<int:id>', views.deletar_comissão),
    path('deletar_todos/', views.deletar_todos),
    path('petição/<int:id>', views.petição),
 
]
    