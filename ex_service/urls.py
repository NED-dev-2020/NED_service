from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="accueil"),
    path('contact/', views.contact, name="contact"),
    path('galerie/', views.galerie, name="galerie"),
    path('a-propos/', views.a_propos, name="a_propos"),
   
]
