import pyautogui
import time
from hehe import cords
def is_color_similar(pixel, target, tolerance=5):
    r, g, b = pixel
    tr, tg, tb = target
    return (
        abs(r - tr) <= tolerance and
        abs(g - tg) <= tolerance and
        abs(b - tb) <= tolerance
    )


def pointmaker(topleft,bottomright):
    points = []
    count = 0 
    dif = ((bottomright[0]-topleft[0])//2, (bottomright[1]-topleft[1])//2)
    for i in range(topleft[0], bottomright[0]+1, dif[0]):
        for j in range(topleft[1], bottomright[1]+1, dif[1]):
            
            points.append((i,j))
    return points




clickcord = pointmaker((744, 1187), (940, 1302))    


print(cords)
print(clickcord)
times = 0
time.sleep(2)
type = 0
while True:
    
   
    pyautogui.write("/")

    pyautogui.write("fish c", interval=0.05)

    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(4)

    pyautogui.click(1028,1339) # click the fish button
    time.sleep(2.5)
    pyautogui.click(934,1378)
        
    # check if we are fishing
    time.sleep(1)
    print("fishing...")
    # middle of the screen
    if is_color_similar(pyautogui.screenshot().getpixel(cords[0]), (19, 43, 63)):
        print(1)
        pyautogui.click(clickcord[0])
    elif is_color_similar(pyautogui.screenshot().getpixel(cords[1]), (19, 43, 63)):
        print(2)
        pyautogui.click(clickcord[1])
    elif is_color_similar(pyautogui.screenshot().getpixel(cords[2]), (19, 43, 62)):
        print(3)
        pyautogui.click(clickcord[2])
    elif is_color_similar(pyautogui.screenshot().getpixel(cords[3]), (18, 42, 64)):
        print(4)
        pyautogui.click(clickcord[3])
    elif is_color_similar(pyautogui.screenshot().getpixel(cords[4]), (21, 43, 63)):
        print(5)
        pyautogui.click(clickcord[4])

    elif is_color_similar(pyautogui.screenshot().getpixel(cords[5]), (18, 44, 65)):
        print(6)
        pyautogui.click(clickcord[5])
    
    
    elif is_color_similar(pyautogui.screenshot().getpixel(cords[6]), (19, 43, 63)):
        print(7)
        pyautogui.click(clickcord[6])

    elif is_color_similar(pyautogui.screenshot().getpixel(cords[7]), (17, 43, 62)):
        print(8)
        pyautogui.click(clickcord[7])
    elif is_color_similar(pyautogui.screenshot().getpixel(cords[8]), (17, 43, 62)):
        print(9)
        pyautogui.click(clickcord[8])
    else:
        print("Could not find the color, skipping...")

    time.sleep(1)
    if type %6 == 0:
        
        pyautogui.write("/")

        pyautogui.write("dig", interval=0.05)

        pyautogui.press("enter")
        
        pyautogui.press("enter")
        time.sleep(2)
        # must wait 2 second for all of them 
    elif type % 6 == 1:
        
        pyautogui.write("/")
    
        pyautogui.write("beg", interval=0.05)

        pyautogui.press("enter")
        
        pyautogui.press("enter")

        time.sleep(2)
        # must wait 2 second for all of them 
    elif type % 6 == 2:
        pyautogui.write("/")

        pyautogui.write("crime", interval=0.05)

        pyautogui.press("enter")
        
        pyautogui.press("enter")
        time.sleep(1.5)
        pyautogui.click(934,1378)
        time.sleep(0.5)
        # must wait 2 second for all of them 
    elif type % 6 == 3:
        pyautogui.click(742,1358)
        pyautogui.write("/")
    
        pyautogui.write("search", interval=0.05)

        pyautogui.press("enter")
        
        pyautogui.press("enter")
        time.sleep(1.5)
        pyautogui.click(934,1378)
        time.sleep(0.5)
        pyautogui.click(742,1358)
        # must wait 2 second for all of them 
    elif type % 6 == 4:


        pyautogui.write("/")
    
        pyautogui.write("hunt", interval=0.05)

        pyautogui.press("enter")
        
        pyautogui.press("enter")
        time.sleep(2)
        # must wait 2 second for all of them 
    elif type % 6 == 5:
        pyautogui.write("/")
    
        pyautogui.write("tidy", interval=0.05)

        pyautogui.press("enter")
        
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.click(876,1336)
        # must wait 2 second for all of them 
        
    type += 1

    times += 1
        
