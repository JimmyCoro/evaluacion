from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    data = {}
    return render(request, 'examen/inicio.html', data)