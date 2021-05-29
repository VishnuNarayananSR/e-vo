from django.shortcuts import render

def voter_registration(request):
    return render(request, 'voter_registration.html')
