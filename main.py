import cv2
import time
from emailing import send_email
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

first_frame = None
status_list = []

while True:
    status = 0
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # calculating the difference in frames, when something enters the camera's view
    # Step 1: capture the first frame
    if first_frame is None:
        first_frame = gray_frame_gau
    # Step 2: calculate the difference in frames
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    cv2.imshow("My Video", dil_frame)  # shows a picture of the thing that entered the camera view, because the
    # that frame is different from the "first_frame" that was initially captured

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # making a rectangle around a detected image
    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if rectangle.any():
            status = 1
    # send email when the image exists camera view
    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[0] == 1 and status_list[1] == 0:
        send_email()

    cv2.imshow("video", frame)
    key = cv2.waitKey(1)

    if key == ord("q"):
        break
video.release()