from django.http import HttpResponse
from django.shortcuts import render
from web3 import Web3
import os
import json

from ethereum.scripts import deploy
deploy.main() 


def homepage(request):
    # return render(request, 'index.html', {'candidate':candidatelist})
    return render(request, 'base_layout.html')

def vote(request):
    return render(request, 'index.html')
