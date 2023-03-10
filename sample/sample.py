import cv2
from tkinter import Tk

WINNAME = 'miniLab'

cam = cv2.VideoCapture(0)
tk = Tk()

while True:
    status, frame = cam.read()

    if not status or cv2.waitKey(1) == ord('q'):
        break

    cv2.circle(frame, (150, 450), 150, (0, 255, 0), thickness=2, lineType=cv2.LINE_4)
    cv2.resizeWindow(winname=WINNAME, width= tk.winfo_width(), height= tk.winfo_height())
    cv2.imshow(winname=WINNAME, mat=frame)