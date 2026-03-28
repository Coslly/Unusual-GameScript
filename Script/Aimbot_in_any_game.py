from torch import clamp
from ultralytics import YOLO
import numpy
import cv2,time,mss,math,keyboard
import pygetwindow
import win32api,win32con
print("Loading model...")
YOLOPose_Model = YOLO("yolo26m-pose.pt").to('cuda')
print("Model loading complete!!!")

GameWindowTitle = str(input("Please enter the game window title(ex: Counter-Strike 3): "))
DetectRange = int(input("Please enter the cropping area(ex: 100~500): "))
TriggerKey = str(input("Please enter the aimbot trigger key(ex: f,a,b,c): "))

with mss.mss() as sct:
     print("To ensure proper operation, please open this program while the game is running.")
     TargetWindow = pygetwindow.getWindowsWithTitle(GameWindowTitle)[0]
     while True:
         screenshot = sct.grab({"top": TargetWindow.top + DetectRange,"left": TargetWindow.left + DetectRange,"width": TargetWindow.width - DetectRange * 2,"height": TargetWindow.height - DetectRange * 2})
         results = YOLOPose_Model(cv2.cvtColor(numpy.array(screenshot), cv2.COLOR_BGRA2BGR), verbose=False)#imgsz=2048

         if keyboard.is_pressed(TriggerKey):
             MinFOV = 1337
             MovingPos = [0,0]
             for person in results[0].keypoints:
                 HeadPos = [person.xy[0,0,0].item(),person.xy[0,0,1].item() - 10]
                 MiddPos = [(TargetWindow.width - DetectRange * 2)/2,(TargetWindow.height - DetectRange * 2)/2]
                 XY_Dis = [HeadPos[0] - MiddPos[0],HeadPos[1] - MiddPos[1]]
                 FOVDis = math.hypot(XY_Dis[0], XY_Dis[1])
                 if MinFOV > FOVDis:
                     MovingPos = XY_Dis
                     MinFOV = FOVDis

             Threshold = 50
             if MovingPos[0] > Threshold:MovingPos[0] = Threshold
             elif MovingPos[0] < -Threshold:MovingPos[0] = -Threshold
             if MovingPos[1] > Threshold:MovingPos[1] = Threshold
             elif MovingPos[1] < -Threshold:MovingPos[1] = -Threshold
             win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(MovingPos[0] * 3), int(MovingPos[1] * 3), 0, 0)
             #print("Mouse moving: " + str(MovingPos[0]) + ", " + str(MovingPos[1]))

         WindowName = "YOLO Aimbot Test Window"
         cv2.imshow(WindowName, results[0].plot())
         if cv2.waitKey(1) == 27 or cv2.getWindowProperty(WindowName, cv2.WND_PROP_VISIBLE) < 1:break
cv2.destroyAllWindows()
exit