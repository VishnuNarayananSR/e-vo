from django.shortcuts import redirect, render, HttpResponse
from .forms import CandidateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
import utils

@login_required(login_url='/candidates/admin_login')
def register(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        name = form['name'].value()
        constituency = form['constituency'].value()
        symbol = form['symbol'].value()
        if form.is_valid():
            contract, tx_details, exceptions = utils.contract(admin=True)
            try:
                contract.createCandidate(name, constituency, symbol, tx_details)
            except exceptions.VirtualMachineError as e:
                return HttpResponse(e.revert_msg)
            return HttpResponse('Candidate Registered.')
    else:
         form = CandidateForm()
    return(render(request, 'candidate_registration.html', {'form':form}))

def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('candidates:admin_home')
    else:
        form = AuthenticationForm()
        return render(request, 'admin_login.html', {'form':form})

def admin_logout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('candidates:admin_login')


def start_election(request):
    if request.method == 'POST':
        contract, tx_details, exceptions = utils.contract(admin=True)
        try:
            contract.startElection(tx_details)
        except exceptions.VirtualMachineError as e:
            return HttpResponse(e.revert_msg)
    return HttpResponse('Election Started.')

def end_election(request):
    if request.method == 'POST':
        contract, tx_details, exceptions = utils.contract(admin=True)
        try:
            contract.endElection(tx_details)
        except exceptions.VirtualMachineError as e:
            return HttpResponse(e.revert_msg)
    return HttpResponse('Election Stopped.')

@login_required(login_url='/candidates/admin_login')
def admin_home(request):
    contract, tx_details, exceptions = utils.contract(admin=True)
    election_state = contract.getElectionState(tx_details)
    print(election_state)
    return render(request, 'admin_home.html', {'is_election_on':election_state})