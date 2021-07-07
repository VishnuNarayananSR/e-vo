from django.http import HttpResponse
from django.shortcuts import redirect, render
from web3 import Web3
import os
import json

from ethereum.scripts import deploy
deploy.main() 


def homepage(request):
    # return render(request, 'index.html', {'candidate':candidatelist})
    # return render(request, 'base_layout.html')
    return redirect('/voters/register')

def vote(request):
    return render(request, 'index.html')
