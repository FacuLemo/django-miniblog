from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("HOLA")


def about(request):
    return HttpResponse("Acerca de")
