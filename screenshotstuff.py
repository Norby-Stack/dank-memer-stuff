import pyautogui
import cv2
import numpy as np

# Example dot positions
points = [
    (794, 965), 
    (965, 759),
    (964, 611),
    (1140, 788),
    (792, 790),
    (1139, 616),
    (791, 613),
    (1141, 962)
    ]

img = pyautogui.screenshot()
img = np.array(img)
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

for x, y in points:
    # draw dot
    cv2.circle(img, (x, y), 4, (0, 0, 255), -1)

    # d raw coordinate text
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

cv2.imshow("Dots", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
