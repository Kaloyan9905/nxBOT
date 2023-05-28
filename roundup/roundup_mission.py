import pyautogui
from pynput.mouse import Controller

from mission.mission import Mission
from mixins.start_app import StartAppMixin


class RoundupMission(StartAppMixin, Mission):
    def __init__(self):
        super().__init__()

    @staticmethod
    def scroll_down_mission_menu(x, y):
        mouse = Controller()

        pyautogui.sleep(3)
        pyautogui.moveTo(x, y)
        pyautogui.sleep(1)

        # Scroll once down
        mouse.scroll(0, -1)
        return 'scrolled down'

