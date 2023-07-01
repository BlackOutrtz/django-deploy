from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('ator/detalhes/<int:ator_id>', views.detalhes, name='detalhes'),
    path('ator/<int:ator_id>/update/', views.update, name='update'),
    path('ator/<int:ator_id>/delete/', views.delete, name='delete'),
    path('ator/create/', views.create, name='create'),
]
