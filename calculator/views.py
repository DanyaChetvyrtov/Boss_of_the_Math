from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def calc(request):
    return render(request, 'calc.html')


def matrix_calc(request):
    return render(request, 'matrix_calc.html')
