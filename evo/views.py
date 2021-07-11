from django.http import HttpResponse
from django.shortcuts import redirect, render
import random 
import cv2
import imutils
from face_auth import f_liveness_detection
from face_auth import questions
import time
import types
from brownie import network
network.connect('gui')

def homepage(request):
    return redirect('/voters/register')

def vote(request):
    return render(request, 'index.html')

from django.http.response import StreamingHttpResponse
from face_auth.camera import Camera

def gen(camera):
	cam = camera.video
	def frame_tobytes(image):
		ret, jpeg = cv2.imencode(".jpg", image)
		return jpeg.tobytes()

	def show_image(cam,text,color = (0,0,255)):
		_, im = cam.read()
		cv2.putText(im,text,(10,50),cv2.FONT_HERSHEY_COMPLEX,1,color,2)
		return im
		
	while True:
		COUNTER, TOTAL = 0,0
		counter_ok_questions = 0
		counter_ok_consecutives = 0
		limit_consecutives = 3
		limit_questions = 3
		counter_try = 0
		limit_try = 50

		for i in range(0,limit_questions):
			# return "success"
			index_question = random.randint(0,3)
			question = questions.question_bank(index_question)
			im = show_image(cam,question)
			yield (b'--frame\r\n'
						b'Content-Type: image/jpeg\r\n\r\n' + frame_tobytes(im) + b'\r\n\r\n')


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
				yield (b'--frame\r\n'
						b'Content-Type: image/jpeg\r\n\r\n' + frame_tobytes(im) + b'\r\n\r\n')

				if challenge_res == "pass":
					im = show_image(cam,question+" : ok")
					yield (b'--frame\r\n'
						b'Content-Type: image/jpeg\r\n\r\n' + frame_tobytes(im) + b'\r\n\r\n')

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
				while True:
					im = show_image(cam,"LIFENESS SUCCESSFUL",color = (0,255,0))
					yield (b'--frame\r\n'
						b'Content-Type: image/jpeg\r\n\r\n' + frame_tobytes(im) + b'\r\n\r\n')
					# time.sleep(1)
					# return("success")
					
			elif i_try == limit_try-1:
				while True:
					im = show_image(cam,"LIFENESS FAIL")
					yield (b'--frame\r\n'
						b'Content-Type: image/jpeg\r\n\r\n' + frame_tobytes(im) + b'\r\n\r\n')					 
					# time.sleep(1)
					# return("fail")
			else:
				continue

		
def cam_stream(request):
	try:
		res = gen(Camera())
		if res == "success":
			return redirect("voters:vote")
		elif res == "fail":
			return HttpResponse("Permission Denied")
		else:
			return StreamingHttpResponse(res,
						content_type='multipart/x-mixed-replace; boundary=frame')
	except StopIteration as e:
		return HttpResponse("404")
def cam_page(request):
	return render(request, "video.html")