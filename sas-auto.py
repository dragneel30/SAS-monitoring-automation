import pyautogui
import time
import os
import sys

def findAndClick(needleFile):
    res = pyautogui.locateOnScreen(needleFile)
    if res is not None:
        pyautogui.click(res[0], res[1])
        return True
    return False
        
def waitAndFindAndClick(needleFile, seconds):
    a = 0   
    while(a < seconds):
        time.sleep(5)
        pyautogui.moveTo(a, 0)
        a = a + 5
        findAndClick("/home/pi/sas-auto/needleNewRefresh")
    if findAndClick(needleFile) == False:
        waitAndFindAndClick(needleFile, seconds)


pyautogui.FAILSAFE = False

while(findAndClick("/home/pi/sas-auto/needleLogin") == False):
    a = 0
while(findAndClick("/home/pi/sas-auto/needleReport") == False):
    a = 0
while(findAndClick("/home/pi/sas-auto/needleHauling") == False):
    a = 0
while(True):
    waitAndFindAndClick("/home/pi/sas-auto/needleBurger", 900)
    findAndClick("/home/pi/sas-auto/needleRefresh")
    

