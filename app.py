import cv2
import streamlit as st
from cvzone.HandTrackingModule import HandDetector
import controller as cnt

# Streamlit App
st.title("Finger Counter and LED Controller")

# Initialize hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Initialize video capture
video = cv2.VideoCapture(0)

if not video.isOpened():
    st.error("Unable to access webcam.")
else:
    st.success("Webcam initialized.")

# Process frames
run = st.checkbox("Start Webcam")
frame_placeholder = st.empty()

while run:
    ret, frame = video.read()
    if not ret:
        st.error("Failed to capture frame from webcam.")
        break

    # Flip frame and process hands
    frame = cv2.flip(frame, 1)
    hands, img = detector.findHands(frame)
    if hands:
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)
        cnt.led(fingerUp)

        # Add finger count text
        finger_count = sum(fingerUp)
        cv2.putText(frame, f"Finger count: {finger_count}", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

    # Display frame in Streamlit
    frame_placeholder.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB")

# Release video capture
video.release()
cv2.destroyAllWindows()
