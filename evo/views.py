from django.http import HttpResponse
from django.shortcuts import redirect, render
from brownie import network
network.connect('gui')

def homepage(request):
    return redirect('/voters/register')

def vote(request):
    return render(request, 'index.html')