import cv2
import controller as cnt
from cvzone.HandTrackingModule import HandDetector
import streamlit as st

# Initialize Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Streamlit UI
st.title("Finger Count and LED Control App")
st.subheader("Real-time Finger Detection with LED Control")

# OpenCV Video Capture
video = cv2.VideoCapture(0)
st_frame = st.empty()

while True:
    ret, frame = video.read()
    if not ret:
        st.error("Error accessing the webcam. Make sure it's connected.")
        break

    frame = cv2.flip(frame, 1)
    hands, img = detector.findHands(frame)

    if hands:
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)

        cnt.led(fingerUp)  # Update LED states via Arduino

        # Display finger count on the frame
        if fingerUp == [0, 0, 0, 0, 0]:
            cv2.putText(frame, 'Finger count: 0', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [0, 1, 0, 0, 0]:
            cv2.putText(frame, 'Finger count: 1', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [0, 1, 1, 0, 0]:
            cv2.putText(frame, 'Finger count: 2', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [0, 1, 1, 1, 0]:
            cv2.putText(frame, 'Finger count: 3', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [0, 1, 1, 1, 1]:
            cv2.putText(frame, 'Finger count: 4', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [1, 1, 1, 1, 1]:
            cv2.putText(frame, 'Finger count: 5', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

    # Display the video stream in Streamlit
    st_frame.image(frame, channels="BGR")

    if st.button("Stop"):
        break

video.release()
cv2.destroyAllWindows()
