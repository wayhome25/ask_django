# dojo/views.py
from django.http import HttpResponse
from django.shortcuts import render

# def mysum(request, x, y=0, z=0):
#     return HttpResponse(int(x) + int(y) + int(z))

def mysum(request, numbers):
    return HttpResponse(sum(map(lambda s: int(s or 0),numbers.split('/'))))

def myname(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요'.format(name,age))
