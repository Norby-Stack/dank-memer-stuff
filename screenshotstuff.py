import pyautogui
import cv2
import numpy as np

topleft = (515, 335)
bottomright = (863, 684)



points = []


ratiox = (60)/116
ratioy = (68)/116

distance = bottomright[0] - topleft[0]

serpatedistance = distance // 3
print(serpatedistance)
for i in range(3):
    for r in range(3):
        points.append((topleft[0] + serpatedistance * i, topleft[1] + serpatedistance * r))



img = pyautogui.screenshot()
img = np.array(img)
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

for x, y in points:
    x, y = int(x+ratiox*serpatedistance),int(y+ratioy*serpatedistance)
    # draw dot
    cv2.circle(img, (x, y), 4, (0, 0, 255), -1)

    # draw coordinate text
    text = f"({x}, {y})"
    cv2.putText(
        img,
        text,
        (x + 6, y - 6),              # offset so it doesn't overlap dot
        cv2.FONT_HERSHEY_SIMPLEX,
        0.35,                        # small font
        (0, 0, 255),                 # red
        1,
        cv2.LINE_AA
    )

cv2.imshow("Dots with Coordinates", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
