from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return HttpResponse("Здесь будет список ситуаций")

def diary (request):
    return HttpResponse("Здесь будет ситуация и ее эмоции")
