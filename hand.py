import cv2

import mediapipe as mp

import time

import pyautogui

import tkinter


cap = cv2.VideoCapture(0)
pTime=0
prev = 0
tres = 20
should =0

mpPose = mp.solutions.pose

pose = mpPose.Pose()

mpDraw =mp.solutions.drawing_utils

while True:
    lmlist = []
    success,img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h,w,c = img.shape

            cx, cy = int(lm.x * w) , int(lm.y * h)
            lmlist.append([id, cx,cy])

            cv2.circle(img, (cx,cy), 10, (255,0,0), cv2.FILLED)
    

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime=cTime
    

    cv2.putText(img, str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)

    cv2.imshow("img",img)


    
    
    currs = lmlist[12][2]
    curr = lmlist[16][2]
    mov = curr - prev
    prev = curr
    movs = currs - should
    should = currs

    relb = lmlist[14][2]

    mid = (lmlist[11][2]+lmlist[23][2])/2
    


      
    if mov < 0 and abs(mov) > tres and relb < mid:
             pyautogui.scroll(abs(mov)*-5)
            
         
         
    if mov > 0 and abs(mov) > tres and movs > 0 and relb < mid  :

             pyautogui.scroll(abs(mov)*5)
     



       
      
       
        
   
      
      
       

    cv2.waitKey(4)


    


