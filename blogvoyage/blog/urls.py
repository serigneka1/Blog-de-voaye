from django.urls import path
from . import views

urlpatterns = [
    path('rechercher/', views.search, name='rechercher'),
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail'),
]


### arrete à 1h21min56s
# admin
# fonction rechercher