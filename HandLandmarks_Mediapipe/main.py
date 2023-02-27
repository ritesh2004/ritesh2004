#from tkinter import Frame
#from tkinter import Y
import cv2 as cv 
import mediapipe as mp 
import pyautogui
import datetime
mp_drawing = mp.solutions.drawing_utils
mp_style = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
screen_height,screen_width = pyautogui.size()
cap = cv.VideoCapture(0)
with mp_hands.Hands(
                    model_complexity = 0,
                    min_tracking_confidence = 0.5,
                    min_detection_confidence = 0.5) as hands:
    while True:
        _,frame = cap.read()
        originalCopy = frame.copy()
        output = hands.process(frame)
        frame_height,frame_width,_ = frame.shape
        frame.flags.writeable = True
        image = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
        if output.multi_hand_landmarks:
            for hand_landmarks in output.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_style.get_default_hand_landmarks_style(),
                    mp_style.get_default_hand_connections_style()
                )
                landmarks = hand_landmarks.landmark
                for id,landmark in enumerate(landmarks):
                    x = int(landmark.x*frame_width)
                    y = int(landmark.y*frame_height)
                    if id == 8:
                        cv.circle(img=frame, center=(x,y),radius=10,color=(0,255,255) )
                        index_x = screen_width/frame_width*x
                        index_y = screen_height/frame_height*y
                    elif id == 12:
                        cv.circle(img=frame, center=(x,y),radius=10,color=(0,255,255) )
                        middle_x = screen_width/frame_width*x
                        middle_y = screen_height/frame_height*y
                        
                        time_stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
                        #print(abs(index_x-middle_x))
                        if abs(index_x-middle_x) > 146:
                            cv.imwrite(f"C:\\Users\\rites\\Pictures\\{time_stamp}.jpg", originalCopy)
                            print("Click")
        cv.imshow("Hand Detection", frame)
        if cv.waitKey(5) == ord("q"):
            break
cap.release()
