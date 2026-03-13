import pyautogui
import time
from hehe import cords
def is_color_similar(pixel, target, tolerance=10):
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


cords = pointmaker((788, 689), (1134, 1043))
color = (18, 42, 65)



clickcord = pointmaker((743, 1255), (952, 1376))    

times = 0
time.sleep(2)
type = 1

while True:
    if type % 50 == 0:
        pyautogui.write("/")

        pyautogui.write("fish bu", interval=0.05)

        pyautogui.press("enter")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.click(950,1402) # bucket sell system
        time.sleep(2)
        pyautogui.click(1217,1375)
        time.sleep(2)
   
    pyautogui.write("/")

    pyautogui.write("fish c", interval=0.05)

    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.press("enter")

    end = time.time()
    # waiting for restart fishing
    if type != 1:
        print("yteeee")
        waittime = 7.5-(end - start)
        time.sleep(max(0, waittime))  # Ensure we don't sleep a negative time
        
    # clicking start
    reruns = 0
    while True:
        time.sleep(0.25)
        
        if pyautogui.screenshot().getpixel((1087, 1410)) ==  (0, 133, 69):
            time.sleep(0.2)
            pyautogui.click(1087, 1410) # click the start
            break
        reruns += 1
        if reruns > 20:  # If it takes too long, break to avoid
            
            break
    
    reruns = 0
    while True:
        time.sleep(0.25)
        
        if is_color_similar(pyautogui.screenshot().getpixel((708, 608)), (33, 73, 108), tolerance=5) or is_color_similar(pyautogui.screenshot().getpixel((706, 387)), (33, 73, 107), tolerance=5) :
            time.sleep(0.2)
            pyautogui.click(958, 1447) # click any notification
            
            break
        reruns += 1
        if reruns > 20:  # If it takes too long, break to avoid
            
            break
    
    
    print("fishing...")
    # middle of the screen
    if is_color_similar(pyautogui.screenshot().getpixel(cords[0]), color):
        print(1)
        pyautogui.click(clickcord[0])
    elif is_color_similar(pyautogui.screenshot().getpixel(cords[1]), color):
        print(2)
        pyautogui.click(clickcord[1])
    elif is_color_similar(pyautogui.screenshot().getpixel(cords[2]), color):
        print(3)
        pyautogui.click(clickcord[2])
    elif is_color_similar(pyautogui.screenshot().getpixel(cords[3]), color):
        print(4)
        pyautogui.click(clickcord[3])
    elif is_color_similar(pyautogui.screenshot().getpixel(cords[4]), color):
        print(5)
        pyautogui.click(clickcord[4])

    elif is_color_similar(pyautogui.screenshot().getpixel(cords[5]), color):
        print(6)
        pyautogui.click(clickcord[5])
    
    
    elif is_color_similar(pyautogui.screenshot().getpixel(cords[6]), color):
        print(7)
        pyautogui.click(clickcord[6])

    elif is_color_similar(pyautogui.screenshot().getpixel(cords[7]), color):
        print(8)
        pyautogui.click(clickcord[7])
    elif is_color_similar(pyautogui.screenshot().getpixel(cords[8]), color):
        print(9)
        pyautogui.click(clickcord[8])
    else:
        print("Could not find the color, skipping...")
    start = time.time()





    time.sleep(1.5)
    if type %6 == 0:
        
        pyautogui.write("/")

        pyautogui.write("dig", interval=0.05)

        pyautogui.press("enter")
        
        pyautogui.press("enter")
        
    
    elif type % 6 == 1:
        
        pyautogui.write("/")
    
        pyautogui.write("beg", interval=0.05)

        pyautogui.press("enter")
        
        pyautogui.press("enter")
        time.sleep(3.5)

        
    elif type % 6 == 2:
        pyautogui.write("/")

        pyautogui.write("post", interval=0.05)

        pyautogui.press("enter")
        
        pyautogui.press("enter")
        time.sleep(3.5)
        pyautogui.click(699,1432)

        
    elif type % 6 == 3:
        
        pyautogui.write("/")
    
        pyautogui.write("search", interval=0.05)

        pyautogui.press("enter")
        
        pyautogui.press("enter")
        time.sleep(3.5)
        pyautogui.click(694,1434)
    elif type % 6 == 4:


        pyautogui.write("/")
    
        pyautogui.write("hunt", interval=0.05)

        pyautogui.press("enter")
        
        pyautogui.press("enter")
        
    elif type % 6 == 5:
        pyautogui.write("/")
    
        pyautogui.write("tidy", interval=0.05)

        pyautogui.press("enter")
        
        pyautogui.press("enter")
        time.sleep(3.5)
        pyautogui.click(884,1406)
    time.sleep(1)
        
    type += 1

    times += 1
        
