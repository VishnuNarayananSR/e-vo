from deepface import DeepFace 
import os

def handle_uploaded_file(f, dest):
    with open("assets/" + dest, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return dest
DIR_NAME = "assets/voters"

def verify(voter_id, live_img):
    img = voter_id + ".jpg"
    img = os.path.join(DIR_NAME, img)
    if os.path.exists(img):
        if (DeepFace.verify(img, live_img, enforce_detection=False)):
            return "True"
        else:
            return "False"
    else:
        return "Missing"