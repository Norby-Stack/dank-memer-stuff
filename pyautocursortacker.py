import pyautogui
from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:  # Only trigger on mouse press, not release
        # Get pixel color at cursor position
        color = pyautogui.screenshot().getpixel((x, y))
        print(f"X: {x}, Y: {y}, Color: {color}")

# Start listening to mouse clicks
with mouse.Listener(on_click=on_click) as listener:
    print("Click anywhere on the screen to print X, Y, and color. Press Ctrl+C to stop.")
    listener.join()
