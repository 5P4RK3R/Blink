# import streamlit as st
# import cv2
# import dlib

# # Load the pre-trained facial landmark detector
# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# def detect_blink(gray, rects):
#     for rect in rects:
#         shape = predictor(gray, rect)
#         left_eye_ratio = blink_ratio(shape, [36, 37, 38, 39, 40, 41])
#         right_eye_ratio = blink_ratio(shape, [42, 43, 44, 45, 46, 47])
#         return left_eye_ratio, right_eye_ratio

# def blink_ratio(shape, eye_indices):
#     left = (shape.part(eye_indices[0]).x, shape.part(eye_indices[0]).y)
#     right = (shape.part(eye_indices[3]).x, shape.part(eye_indices[3]).y)
#     top = (shape.part(eye_indices[1]).x, shape.part(eye_indices[1]).y)
#     bottom = (shape.part(eye_indices[4]).x, shape.part(eye_indices[4]).y)
#     center_top = midpoint(left, right)
#     center_bottom = midpoint(top, bottom)
    
#     # Compute the distance between the top and bottom eyelid
#     vertical_distance = cv2.norm(np.array(center_top) - np.array(center_bottom))
    
#     # Compute the distance between the left and right side of the eye
#     horizontal_distance = cv2.norm(np.array(left) - np.array(right))
    
#     ratio = vertical_distance / horizontal_distance
#     return ratio

# def midpoint(p1, p2):
#     return int((p1[0] + p2[0]) / 2), int((p1[1] + p2[1]) / 2)

# def main():
#     st.title("Live Video Stream Blink Detection")

#     # Initialize the video capture
#     cap = cv2.VideoCapture(0)

#     while True:
#         ret, frame = cap.read()

#         # Convert the frame to grayscale for face detection
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         rects = detector(gray, 0)

#         left_eye_ratio, right_eye_ratio = detect_blink(gray, rects)

#         st.write("Left Eye Blink Ratio:", left_eye_ratio)
#         st.write("Right Eye Blink Ratio:", right_eye_ratio)

#         # Display the frame with Streamlit
#         st.image(frame, channels="BGR", use_column_width=True)

# if __name__ == "__main__":
#     main()
import os
import cv2
import streamlit as st
import numpy as np
import tempfile
from core.vision.blink import Blink
# Use this line to capture video from the webcam
# cap = cv2.VideoCapture(0)

os.environ['OPENCV_AVFOUNDATION_SKIP_AUTH'] = '1'
# Set the title for the Streamlit app
st.title("Blink Detection")
run = st.checkbox('Run')

# Add a "Stop" button and store its state in a variable
stop = st.button("Stop")
if run:
    blink = Blink(predictor="shape_predictor_68_face_landmarks.dat")
    # video = st.empty()
    FRAME = st.image([])


    while blink.cap.isOpened() and not stop:
        ret, frame = blink.cap.read()

        if not ret:
            st.write("The video capture has ended.")
            break

        # You can process the frame here if needed
        # e.g., apply filters, transformations, or object detection

        # Convert the frame from BGR to RGB format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = blink.detect(frame)

        # Display the frame using Streamlit's st.image
        # video.image(frame, channels="RGB")
        FRAME.image(frame)

        # Break the loop if the 'q' key is pressed or the user clicks the "Stop" button
        if cv2.waitKey(1) & 0xFF == ord("q") or stop: 
            break

    blink.cap.release()
    cv2.destroyAllWindows()