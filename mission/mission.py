import os
import pyautogui

from abc import ABC


class Mission(ABC):
    def __init__(self):
        pass

    @staticmethod
    def trigger_image_recognition(image_file, x, y):
        pyautogui.sleep(3)

        while True:
            if pyautogui.locateOnScreen(image_file) is not None:
                pyautogui.click(x, y)
                return 'works'
            else:
                image_name = os.path.splitext(os.path.basename(image_file))[0]
                print(f"{image_name} not found on the screen.")
                pyautogui.sleep(1)

    @staticmethod
    def trigger_image_recognition_and_click_on_it(image_file):
        pyautogui.sleep(3)

        while True:
            if pyautogui.locateOnScreen(image_file) is not None:
                image_location = pyautogui.locateOnScreen(image_file)
                # Get the center coordinates of the image
                center_x = image_location.left + (image_location.width // 2)
                center_y = image_location.top + (image_location.height // 2)

                # Move the mouse to the center coordinates and perform a click
                pyautogui.click(center_x, center_y)
                return 'works'
            else:
                image_name = os.path.splitext(os.path.basename(image_file))[0]
                print(f"{image_name} not found on the screen.")
                pyautogui.sleep(1)

    @staticmethod
    def mouse_click_and_slide(start_x, start_y, end_x, end_y):
        pyautogui.sleep(3)

        try:
            # Move the mouse to the starting position and perform a mouse down action
            pyautogui.moveTo(start_x, start_y)
            pyautogui.mouseDown()

            # Move the mouse to the ending position
            pyautogui.moveTo(end_x, end_y)

            # Delay to hold the mouse button (adjust as needed)
            pyautogui.sleep(1)

            # Release the mouse button
            pyautogui.mouseUp()

        except Exception as e:
            return f'Error while performing mouse action: {e}'
