from django.urls import path
from . import views
from .views import iletisim_view

urlpatterns = [
    path('', views.index, name='index'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('iletisim/', iletisim_view, name='iletisim'),
    path('ilanlar/', views.all_properties, name='all_properties'),
]

