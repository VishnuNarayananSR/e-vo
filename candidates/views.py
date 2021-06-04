from django.shortcuts import redirect, render, HttpResponse
from .forms import CandidateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
import utils


@login_required(login_url="/candidates/admin_login")
def register(request):
    if request.method == "POST":
        form = CandidateForm(request.POST, request.FILES)
        name = form["name"].value()
        constituency = form["constituency"].value()
        if form.is_valid():
            symbol_file_dest = "symbols/" + name + ".jpg"
            contract, tx_details, exceptions = utils.contract(admin=True)
            try:
                contract.createCandidate(
                    name, constituency, symbol_file_dest, tx_details
                )
                handle_uploaded_file(
                request.FILES["symbol"], symbol_file_dest  # do better naming
            )
            except exceptions.VirtualMachineError as e:
                messages.error(request, e.revert_msg)
                return redirect(request.path)
            messages.success(request, "Candidate Registered.")
            return redirect(request.path)
        messages.error(request, form.errors.as_text())
        return redirect(request.path)
    else:
        form = CandidateForm()
    return render(request, "candidate_registration.html", {"form": form})


def handle_uploaded_file(f, dest):
    with open("assets/" + dest, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return dest


def admin_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("candidates:admin_home")
    else:
        form = AuthenticationForm()
        return render(request, "admin_login.html", {"form": form})


def admin_logout(request):
    if request.method == "POST":
        logout(request)
    return redirect("candidates:admin_login")


@login_required(login_url="/candidates/admin_login")
def admin_home(request):
    contract, tx_details, exceptions = utils.contract(admin=True)
    election_state = contract.getElectionState(tx_details)
    candidates = contract.getCandidatesList(tx_details)
    result = None
    if not election_state:
        # if no election progress
        result = candidates
    candidates = list(set(map(lambda c: (c[0], c[2]), candidates)))
    # print(candidates, election_state)
    return render(
        request,
        "admin_home.html",
        {"is_election_on": election_state, "result": result, "candidates": candidates},
    )


def start_election(request):
    if request.method == "POST":
        contract, tx_details, exceptions = utils.contract(admin=True)
        try:
            contract.startElection(tx_details)
        except exceptions.VirtualMachineError as e:
            return JsonResponse({"message": e.revert_msg, "status": "error"})
    return JsonResponse({"message": "Election started", "status": "success"})


def end_election(request):
    if request.method == "POST":
        contract, tx_details, exceptions = utils.contract(admin=True)
        try:
            contract.endElection(tx_details)
        except exceptions.VirtualMachineError as e:
            return JsonResponse({"message": e.revert_msg, "status": "error"})
    return JsonResponse({"message": "Election stopped", "status": "success"})
