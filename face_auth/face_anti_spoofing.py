import random 
import cv2
import imutils
from face_auth import f_liveness_detection
from face_auth import questions

class CamException(Exception):
    pass
class Detection():
    def __init__(self) -> None:
        self.COUNTER, self.TOTAL = 0,0
        self.counter_ok_questions = 0
        self.counter_ok_consecutives = 0
        self.limit_consecutives = 3
        self.limit_questions = 3
        self.counter_try = 0
        self.limit_try = 50 
        print("accessing cam...")
        self.cam = cv2.VideoCapture(-1)
        print("cam captured")
        if self.cam is None or not self.cam.isOpened():
            print("raise cam exception")
            raise CamException
        print("making window")
        cv2.startWindowThread()
        cv2.namedWindow("Face Authentication")
        print("window made")

    def __del__(self):
        print("releasing cam")
        self.cam.release()
        print("cam released")
        cv2.destroyAllWindows()

    def show_image(self,text,color = (0,0,255)):
        ret, im = self.cam.read()
        im = imutils.resize(im, width=720)
        cv2.putText(im,text,(10,50),cv2.FONT_HERSHEY_COMPLEX,1,color,2)
        return im

    def detect(self):
        print("begin detect")
        live_img = None
        for i_questions in range(0,self.limit_questions):
            index_question = random.randint(0,3)
            question = questions.question_bank(index_question)
            
            im = self.show_image(question)
            cv2.imshow('Face Authentication',im)
            if cv2.waitKey(1) &0xFF == ord('q'):
                break 

            for i_try in range(self.limit_try):
                ret, im = self.cam.read()
                im = imutils.resize(im, width=720)
                im = cv2.flip(im, 1)
                TOTAL_0 = self.TOTAL
                out_model = f_liveness_detection.detect_liveness(im,self.COUNTER,TOTAL_0)
                self.TOTAL = out_model['total_blinks']
                self.COUNTER = out_model['count_blinks_consecutives']
                dif_blink = self.TOTAL-TOTAL_0
                if dif_blink > 0:
                    blinks_up = 1
                else:
                    blinks_up = 0

                challenge_res = questions.challenge_result(question, out_model,blinks_up)

                im = self.show_image(question)
                cv2.imshow('Face Authentication',im)
                if cv2.waitKey(1) &0xFF == ord('q'):
                    break 
                live_img = im
                if challenge_res == "pass":
                    im = self.show_image(question+" : ok")
                    cv2.imshow('Face Authentication',im)
                    if cv2.waitKey(1) &0xFF == ord('q'):
                        break

                    self.counter_ok_consecutives += 1
                    if self.counter_ok_consecutives == self.limit_consecutives:
                        self.counter_ok_questions += 1
                        self.counter_try = 0
                        self.counter_ok_consecutives = 0
                        break
                    else:
                        continue

                elif challenge_res == "fail":
                    self.counter_try += 1
                    self.show_image(question+" : fail")
                elif i_try == self.limit_try-1:
                    break
                    

            if self.counter_ok_questions ==  self.limit_questions:
                    im = self.show_image("LIVENESS SUCCESSFUL",color = (0,255,0))
                    cv2.imshow('Face Authentication',im)
                    if cv2.waitKey(3000) &0xFF == ord('q'):
                        break
                    
                    return live_img, True
            elif i_try == self.limit_try-1:
                    im = self.show_image("LIVENESS FAIL")
                    cv2.imshow('Face Authentication',im)
                    if cv2.waitKey(3000) &0xFF == ord('q'):
                        break
                    return live_img, False
            else:
                print("continued")
                continue