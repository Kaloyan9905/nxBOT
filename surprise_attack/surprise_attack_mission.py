import os
import pyautogui

from mission.mission import Mission
from mixins.start_app import StartAppMixin


class SurpriseAttackMission(StartAppMixin, Mission):
    def __init__(self):
        super().__init__()

    @staticmethod
    def trigger_jutsu_image_recognition_and_click_on_it(image_file):
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
                pyautogui.sleep(0.5)
                return 'does not triggered'

