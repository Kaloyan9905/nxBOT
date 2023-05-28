import pyautogui
from pynput import *


def get_coordinates(x, y):
    print(f"X - {x}; Y - {y}")


with mouse.Listener(on_move=get_coordinates) as listen:
    listen.join()
