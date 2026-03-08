import pyautogui
import time
from hehe import cords
def is_color_similar(pixel, target, tolerance=20):
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




clickcord = pointmaker((778, 1235), (995, 1016))    
difs = [(0,0)]

print(cords)
print(clickcord)
times = 0
time.sleep(2)

while True:
    
   
    pyautogui.write("/")

    pyautogui.write("fish c", interval=0.05)

    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(4)

    pyautogui.click(1081,1404)
    time.sleep(2.5)
    pyautogui.click(987,1446)
        
    # check if we are fishing
    time.sleep(0.5)
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

    elif is_color_similar(pyautogui.screenshot().getpixel(cords[7]), (19, 44, 69)):
        print(8)
        pyautogui.click(clickcord[7])
    elif is_color_similar(pyautogui.screenshot().getpixel(cords[8]), (19, 44, 69)):
        print(9)
        pyautogui.click(clickcord[8])
    else:
        print("Could not find the color, skipping...")

    time.sleep(1)
    
    pyautogui.write("/")

    pyautogui.write("dig", interval=0.05)

    pyautogui.press("enter")
    
    pyautogui.press("enter")
    
    pyautogui.write("/")
 
    pyautogui.write("hunt", interval=0.05)

    pyautogui.press("enter")
    
    pyautogui.press("enter")

    pyautogui.write("/")
 
    pyautogui.write("beg", interval=0.05)

    pyautogui.press("enter")
    
    pyautogui.press("enter")

    time.sleep(1)

    times += 1
        
