from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import VoterForm, VoteForm
from django.contrib import messages
import utils
import os 
from face_auth.face_anti_spoofing import Detection
from face_auth import face_recognition

def handle_uploaded_file(f, dest):
    filename = "assets/" + dest
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    with open(filename, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return dest

def voter_registration(request):
    if request.method == "POST":
        form = VoterForm(request.POST, request.FILES)
        name = form["name"].value()
        voter_id = form["voter_id"].value()
        constituency = form["constituency"].value()
        if form.is_valid():
            img_file_dest = "voters/" + voter_id + ".jpg"
            contract, tx_details, exceptions = utils.contract()
            try:
                contract.createVoter(name, voter_id, constituency, tx_details)
                handle_uploaded_file(
                request.FILES["voter_img"], img_file_dest
            )
                messages.success(request, "Voter registered.")
                return redirect(request.path)
            except exceptions.VirtualMachineError as e:
                messages.error(request, e.revert_msg)
                return redirect(request.path)
        # messages.error(request, e.revert_msg) # set field errors
        messages.error(request, form.errors.as_text())
        return redirect(request.path)
    else:
        form = VoterForm()
        return render(request, "voter_registration.html", {"form": form})


def vote(request):
    if request.method == "POST":
        form = VoteForm(request.POST)
        voter_id = form["voter_id"].value()
        constituency = form["constituency"].value()

        vote_for = form["vote_for"].value()
        symbol = form["symbol"].value()

        if form.is_valid():
            try:
                auth = Detection()
                live_img, alive = auth.detect()
                del(auth)
                import cv2
                cv2.destroyAllWindows()
                contract, tx_details, exceptions = utils.contract()
                if alive:
                    face_verified = face_recognition.verify(voter_id, live_img)
                    print("face_verified=",face_verified)
                    if face_verified == "True":
                        try:
                            contract.vote(voter_id, vote_for, constituency, symbol, tx_details)
                        except exceptions.VirtualMachineError as e:
                            messages.error(request, e.revert_msg)
                            return redirect(request.path)
                    elif face_verified == "Missing":
                        messages.error(request, "Missing Face data. Your Face is not registered.")
                        return redirect(request.path)
                    elif face_verified == "False":
                        messages.error(request, "Face data did not match with registered face.")
                        return redirect(request.path)
                else:
                    messages.error(request, "Liveness Detection Failed.")
                    return redirect(request.path)
            except Exception as e:
                print(e)
                messages.error(request, "Some error occured while video authentication. Please try again")
                return redirect(request.path)
            messages.success(request, "Voted Successfully.")
            return redirect(request.path)
        # messages.error(request, e.revert_msg) # set field errors
        messages.error(request, form.errors.as_text())
        return redirect(request.path)
    else:
        contract, tx_details, exceptions = utils.contract()
        candidates = contract.getCandidatesList()  # ?
        candidates = list(set(map(lambda c: (c[0], c[2]), candidates)))
        form = VoteForm()
        return render(request, "vote.html", {"form": form, "candidates": candidates})
