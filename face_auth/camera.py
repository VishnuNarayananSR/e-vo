import cv2
# import threading

class Camera():
    def __init__(self) -> None:
        self.video = cv2.VideoCapture(0)
        # threading.Thread(target=self.get_frame, args=()).start()

    def __del__(self) -> None:
        self.video.release()
