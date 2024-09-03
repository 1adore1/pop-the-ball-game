import cv2
import mediapipe as mp
import numpy as np
import random

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.6, min_tracking_confidence=0.4)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

balls = []
ball_radius = 30

def create_ball():
    x = random.randint(ball_radius, 620)
    y = 0
    return [x, y]

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    
    frame = cv2.flip(frame, 1)
    landmarks = hands.process(frame)

    frame_height, frame_width, _ = frame.shape

    hand_pos = []
    if landmarks.multi_hand_landmarks:
        for hand_landmarks in landmarks.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                x, y = int(lm.x * frame_width), int(lm.y * frame_height)
                hand_pos.append((x, y))
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    if random.random() < 0.05:
        balls.append(create_ball())

    remaining_balls = []
    for i in range(len(balls)):
        balls[i][1] += 5
        cv2.circle(frame, (balls[i][0], balls[i][1]), ball_radius, (0, 255, 0), -1)

        if balls[i][1] - ball_radius < frame_height:
            remaining_balls.append(balls[i])
        
    balls = remaining_balls

    cv2.imshow('game', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()