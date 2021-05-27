from django.shortcuts import render

def candidate(request):
    return(render(request, 'candidateHome.html'))