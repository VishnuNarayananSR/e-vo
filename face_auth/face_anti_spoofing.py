import random 
import cv2
import imutils
from face_auth import f_liveness_detection
from face_auth import questions

class CV():
    def __init__(self) -> None:
        self. cam = cv2.VideoCapture(0)
    def __del__(self):
        self.cam.release()
        cv2.destroyAllWindows()

def show_image(cam,text,color = (0,0,255)):
    ret, im = cam.read()
    im = imutils.resize(im, width=720)
    cv2.putText(im,text,(10,50),cv2.FONT_HERSHEY_COMPLEX,1,color,2)
    return im

def detect():
    cv = CV()
    cam = cv.cam
    COUNTER, TOTAL = 0,0
    counter_ok_questions = 0
    counter_ok_consecutives = 0
    limit_consecutives = 3
    limit_questions = 3
    counter_try = 0
    limit_try = 50 
    live_img = None
    for i_questions in range(0,limit_questions):
        index_question = random.randint(0,3)
        question = questions.question_bank(index_question)
        
        im = show_image(cam,question)
        cv2.imshow('Face Authentication',im)
        if cv2.waitKey(500) &0xFF == ord('q'):
            break 

        for i_try in range(limit_try):
            ret, im = cam.read()
            im = imutils.resize(im, width=720)
            im = cv2.flip(im, 1)
            TOTAL_0 = TOTAL
            out_model = f_liveness_detection.detect_liveness(im,COUNTER,TOTAL_0)
            TOTAL = out_model['total_blinks']
            COUNTER = out_model['count_blinks_consecutives']
            dif_blink = TOTAL-TOTAL_0
            if dif_blink > 0:
                blinks_up = 1
            else:
                blinks_up = 0

            challenge_res = questions.challenge_result(question, out_model,blinks_up)

            im = show_image(cam,question)
            cv2.imshow('Face Authentication',im)
            if cv2.waitKey(1) &0xFF == ord('q'):
                break 
            live_img = im
            if challenge_res == "pass":
                im = show_image(cam,question+" : ok")
                cv2.imshow('Face Authentication',im)
                if cv2.waitKey(1) &0xFF == ord('q'):
                    break

                counter_ok_consecutives += 1
                if counter_ok_consecutives == limit_consecutives:
                    counter_ok_questions += 1
                    counter_try = 0
                    counter_ok_consecutives = 0
                    break
                else:
                    continue

            elif challenge_res == "fail":
                counter_try += 1
                show_image(cam,question+" : fail")
            elif i_try == limit_try-1:
                break
                

        if counter_ok_questions ==  limit_questions:
                im = show_image(cam,"LIVENESS SUCCESSFUL",color = (0,255,0))
                cv2.imshow('Face Authentication',im)
                if cv2.waitKey(3000) &0xFF == ord('q'):
                    break
                return live_img, True
        elif i_try == limit_try-1:
                im = show_image(cam,"LIVENESS FAIL")
                cv2.imshow('Face Authentication',im)
                if cv2.waitKey(3000) &0xFF == ord('q'):
                    break
                return live_img, False
        else:
            continue
