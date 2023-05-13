from django.urls import path
from . import views # importo las vistas de newapp


urlpatterns = [
    path('', views.home),
]