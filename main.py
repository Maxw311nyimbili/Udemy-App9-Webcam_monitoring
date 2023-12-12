import cv2
import time

# the class VideoCapture() is used to capture a video, and putting zero in the
# parenthesis means that you want to use the primary camera on the device. Putting a one in the
# parenthesis means that you want to use a secondary camera to capture the video.
# -----------------video = cv2.VideoCapture(0)-----------------
# -----------------check, frame = video.read()-----------------
# the read method has to values, the check value is of type boolean and returns true or false
# while the frame returns the video as a series of picture pixels

# to show the video, use a method called imshow(), and it should be placed inside a while-loop

video = cv2.VideoCapture(0)
time.sleep(1)  # sets the delay to one second

while True:

    check, frame = video.read()
    cv2.imshow("My Video", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break
video.release()