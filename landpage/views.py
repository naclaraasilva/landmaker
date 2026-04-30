from django.shortcuts import render

def index(request):
    return render(request, 'base.html')

def sobre(request):
    return render(request, 'projetos/sobre.html')