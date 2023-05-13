from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    """
    Function responds to website root HHTP request

    Returns index.html template - no db data returned
    """

    name = "Zander"
    age = 27

    # Imprimir objetos en consola
    # print(name)
    # Imprimir longitud de objetos en consola
    # print(len(name))
    # print(request)
    print("method:", request.method)
    print("GET:", request.GET)
    print("POST:", request.POST)



    # return HttpResponse('Hello, World!')
    return render(request, 'index.html', {'name': name, 'age': age})

