from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm

def addnew(request):

    formset = CustomerForm()

    return render(request, 'addnew.html', {'formset': formset})

# Create your views here.
def home(request):
    """
    Function responds to website root HHTP request

    Returns index.html template - no db data returned
    """

    # name = "Zander"
    # age = 27

    # Imprimir objetos en consola
    # print(name)
    # Imprimir longitud de objetos en consola
    # print(len(name))
    # print(request)
    # print("method:", request.method)
    # print("GET:", request.GET)
    # print("POST:", request.POST)

    x = Customer.objects.all()

    # for value in x:
    #     print(value)
    #     name= value.name
    #     age = value.age

    # return HttpResponse('Hello, World!')
    return render(request, 'index.html', {'data': x})

