import cv2 
import mediapipe as mp
import pydirectinput as pd 

import pyautogui as pg
face_mesh = mp.solutions.face_mesh.FaceMesh(max_num_faces=1)

frame_width = 640
frame_height = 480

landmarks_points = None


cap = cv2.VideoCapture(0)

while True:
    
    _, frame = cap.read()

    frame = cv2.flip(frame,1)
    frame = cv2.resize(frame, (frame_width, frame_height))

    
    new_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    
    output = face_mesh.process(new_frame)
    landmarks_points = output.multi_face_landmarks

    
    if landmarks_points:
        landmarks = landmarks_points[0].landmark

        
        x = int(landmarks[1].x * frame_width)
        z = int(landmarks[1].z * 100)

        if z <-7:
            
            pd.press("up")
        if x > 300:
            pd.press("right")
          
        elif x < 200:
            
            pd.press("left")
            pg.press("left")
 

  
    cv2.imshow("face", frame)

   
    if cv2.waitKey(2) & 0xFF == ord("d"):
        break


cap.release()
cv2.destroyAllWindows()
