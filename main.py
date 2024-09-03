import cv2
import mediapipe as mp
import numpy as np
import random

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.6, min_tracking_confidence=0.4)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    
    frame = cv2.flip(frame, 1)
    landmarks = hands.process(frame)

    frame_height, frame_width, _ = frame.shape

    if landmarks.multi_hand_landmarks:
        for hand_landmarks in landmarks.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow('game', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()