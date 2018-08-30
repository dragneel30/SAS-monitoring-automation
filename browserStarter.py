import pyautogui
import time
import os
import sys



time.sleep(15)
pyautogui.keyDown('alt')
pyautogui.press('f4')
pyautogui.keyUp('alt')


os.system('/usr/bin/chromium-browser --kiosk --no-sandbox --disable-infobars -disable-restore-session-state http://sas-server:1260/SASVisualAnalyticsViewer')
time.sleep(5)


