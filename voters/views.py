from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import VoterForm, VoteForm
import utils


def voter_registration(request):
    if request.method == 'POST':
        form = VoterForm(request.POST)
        name = form['name'].value()
        voter_id = form['voter_id'].value()
        constituency = form['constituency'].value()
        if form.is_valid():
            contract, tx_details, exceptions = utils.contract()
            try:
                contract.createVoter(name, voter_id, constituency, tx_details)
            except exceptions.VirtualMachineError as e:
                return HttpResponse(e.revert_msg)
            return HttpResponse('Voter Registered.')
    else:
         form = VoterForm()
    return render(request, 'voter_registration.html', {'form':form})

def vote(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        voter_id = form['voter_id'].value()
        constituency = form['constituency'].value()
        
        vote_for = form['vote_for'].value()
        symbol = form['symbol'].value()

        if form.is_valid():
            contract, tx_details, exceptions = utils.contract()

            candidates = contract.getCandidatesList(tx_details)
            candidates = list(set(map(lambda c: (c[0], c[2]), candidates)))

            try:
                contract.vote(voter_id, vote_for, constituency, symbol, tx_details)
            except exceptions.VirtualMachineError as e:
                return HttpResponse(e.revert_msg)
            return HttpResponse('Voted Successfully.')
    else:
         form = VoteForm()
    return render(request, 'vote.html', {'form':form})

