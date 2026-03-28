# 😳Unusual-GameScript
Scripts that can run in any game
## 😘Features
- External
- Any game can be used
- Safely
- Simple code
## 🧐Principle
### [C++ Triggerbot](https://github.com/Coslly/Unusual-GameScript/blob/main/Script/Triggerbot%20in%20any%20game/Triggerbot%20in%20any%20game/main.cpp)
Uses the most basic characteristics of screen pixel color change (pixel color selection). When the pixel color change is greater than the set value (default 50), the mouse script operation is performed to simulate a shooting in the game. Therefore, you may fire incorrectly when moving the camera in the game.
![image](https://github.com/Coslly/Unusual-GameScript/blob/main/Show/Triggerbot.gif)
### [Python Aimbot](https://github.com/Coslly/Unusual-GameScript/blob/main/Script/Aimbot_in_any_game.py)
Uses Ultralytics YOLO to detect people and locate their head positions in the game screen, captures the center area to improve speed, selects the target closest to the crosshair, converts the positional offset into mouse movement, and finally moves the cursor to automatically aim toward the target.

To run the aimbot.py, you need to install some lib.
`pip install ultralytics numpy opencv-python mss keyboard pygetwindow pywin32`

![image](https://github.com/Coslly/Unusual-GameScript/blob/main/Show/Aimbot.gif)
# 💀Disclaimer
The Github page of this project does not provide compiled files and is only for educational purposes.

I am not responsible for anything that happens when you use this software.
