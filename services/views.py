from django.shortcuts import render
# importando la funcion httResponse, sino no se puede usar
from django.http import HttpResponse
# funcion index .
def index(request):
    print("soy un log de servidor")
    print("––entrando al index––")
    return HttpResponse("eso ")
