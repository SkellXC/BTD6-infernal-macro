import pyautogui
import time
import keyboard
import random
import win32api, win32con
'''
import pyautogui
pyautogui.displayMousePosition()
(1376,433) is the location of I in infernal

'''
time.sleep(1.5)
print("[+] Script is now running\n[+] Hold q to end the script")
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def openMap():
    if pyautogui.pixel(1267,903)[1] == 232:#Presses 
        click(1267,903)
        print("[+] Pressed the 'Play' Button")
        time.sleep(1)
    if pyautogui.pixel(1871,881)[1] == 218 and pyautogui.pixel(1376,433)[1] != 255:#Opens the expert map section by checking for the skull
        click(1871,881)
        time.sleep(2)
    if pyautogui.pixel(1376,433)[1] != 255 and pyautogui.pixel(1871,881)[1] == 218:#Checks to make sure the correct map is visible by checking for the "I"
        print("[-] Error! Wrong map page opened. Fixing...")#in the word Infernal
        click(1871,881)#I know I repeat the same thing but I'm scared to remove it
    if pyautogui.pixel(1376,433)[1] == 255:
        click(1454,576)#Clicks on the map "Infernal"
        print("[+] Selected the map 'Infernal'")
        time.sleep(2)
    if pyautogui.pixel(1064,395)[0] == 254: 
        click(1064,395)#Selects easy mode
        print("[+] Selected Easy mode")
        time.sleep(2)
    if pyautogui.pixel(1865,403)[0] == 255:
        click(1865,403)
        print("[+] Entering Deflation")
def press(letter):
    keyboard.press(letter)
    time.sleep(0.5)#me lazy
    keyboard.release(letter)
    time.sleep(0.5)
def placeSniper():
    time.sleep(2)
    click(2028,474)#Clicks on snipers position
    time.sleep(1.5)
    press("z")#Places sniper using its hotkey
    time.sleep(1.5)
    click(2028,474)#Clicks again to place
    print("[M] Sniper placed")
    time.sleep(1.5)
    click(2028,474)#Click to upgrade
    time.sleep(1)

    for x in range(0,4):#Upgrades the bottom path of the sniper
        time.sleep(0.5)
        click(900,800)
    time.sleep(1)
    for x in range(0,4):#Constant issues with keypresses plus
        press(".")      #long process of location led me to just have
        time.sleep(0.5) #it pressed a bunch of times incase it misses
        #print(f". Number {x}")
    print("[M] Sniper has been upgraded")
#----------------------------------------------------------------------#    
def placeVillage():
    time.sleep(2)
    click(2006,637)#Location for village
    time.sleep(0.5)
    press("k")
    time.sleep(1.5)
    click(2006,637)#Places it, Location doesn't matter
    print("[M] Village Placed")
    time.sleep(1.5)
    click(2006,637)#Opens upgrade menu
    time.sleep(1)
    for x in range(0,2):#Upgrades
        click(900,500)
        time.sleep(0.5)
    print("[M] Village Upgraded")

#----------------------------------------------------------------------#  
def placeAlch():
    time.sleep(2)
    click(2026,527)#Selects location
    time.sleep(0.5)
    press("f")
    time.sleep(1.5)
    click(2026,527)#Places it down
    print("[M] Alchemist Placed")
    time.sleep(1.5)
    click(2026,527)#Opens upgrade menu
    time.sleep(0.5)
    for x in range(0,4):#Upgrades top path
        click(900,500)
        time.sleep(0.5)
    for x in range(0,2):#Upgrades middle path
        click(900,700)
        time.sleep(0.5)
    print("[M] Alchemist Upgraded")

#----------------------------------------------------------------------#  

def gameStart():
    time.sleep(0.5)
    click(2300,1000)
    time.sleep(0.5)
    click(2300,1000)
    print("[G] Game has started")

def defeatCheck():
    if pyautogui.pixel(1376,433)[0] <= 251:
        return True
def restartGame():
    if pyautogui.pixel(1376,433)[0] <= 251:
        click(1200,800)#Clicks the "Home" Button when you lose
        #click(1450,839)#Clicks the "Restart" Button when you lose
        print("[G] Game Lost! Restarting...")
def gameWon():
    time.sleep(0.4)
    if pyautogui.pixel(1500,939)[2] == 255:
        print("[G] Game won")
        click(1500,939)
        time.sleep(1)
        click(1200,830)
        print("[G] Restarting")
        time.sleep(5)
    else:
        print("B")

def process():
    openMap()
    time.sleep(10)
    placeSniper()
    placeVillage()
    placeAlch()
    gameStart()
    time.sleep(2)
    while pyautogui.pixel(1500,939)[0] != 255:
        gameWon()


game = False
while keyboard.is_pressed("q") == False:
    process()

print("[-] Script is no longer running")
