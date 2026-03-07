import pyautogui
import time

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
            if count != 8:
                count +=1
                points.append((i,j))
    return points



cords = pointmaker((791, 611), (1141, 962))

print(cords)
print(cords)
times = 0
time.sleep(2)

while True:
    
   
    pyautogui.write("/")

    pyautogui.write("fish c", interval=0.05)

    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(2)

    pyautogui.click(1081,1404)
   
        
    # check if we are fishing
    time.sleep(4)
    print("fishing...")
    # middle of the screen
    if is_color_similar(pyautogui.screenshot().getpixel((794, 965)), (19, 43, 63), 5):
        print("1 1")
        pyautogui.click(750,1294)
    elif is_color_similar(pyautogui.screenshot().getpixel((965, 759)), (19, 43, 63), 5):
        print("2 2")
        pyautogui.click(850,1239)
    elif is_color_similar(pyautogui.screenshot().getpixel((964, 611)), (19, 43, 62), 5):
        print("2 3")
        print("Found the color, clicking!")
        pyautogui.click(850,1180)
    elif is_color_similar(pyautogui.screenshot().getpixel((1140, 788)), (18, 42, 64), 5):
        print("3 2")
        pyautogui.click(953,1238)
    elif is_color_similar(pyautogui.screenshot().getpixel((792, 790)), (21, 43, 63), 5):
        print("1 2")
        pyautogui.click(744,1237)

    elif is_color_similar(pyautogui.screenshot().getpixel((1139, 616)), (18, 44, 65), 5):
        print("3 3")
        pyautogui.click(960,1181)
    
    
    elif is_color_similar(pyautogui.screenshot().getpixel((791, 613)), (19, 43, 63), 5):
        print("1 3")
        pyautogui.click(743,1181)

    elif is_color_similar(pyautogui.screenshot().getpixel((1141, 962)), (19, 44, 69), 5):
        print("3 1")
        pyautogui.click(948,1302)

    
    time.sleep(3)
    pyautogui.write("/")

    pyautogui.write("dig", interval=0.05)

    pyautogui.press("enter")
    
    pyautogui.press("enter")
    
    pyautogui.write("/")
 
    pyautogui.write("hunt", interval=0.05)

    pyautogui.press("enter")
    
    pyautogui.press("enter")
    time.sleep(1)

    times += 1
        
