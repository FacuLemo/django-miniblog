from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("ANDA A /PRODUCTS :)")


def about(request):
    return HttpResponse("Acerca de")
