import pyautogui


class StartAppMixin:
    X = 114
    Y = 31

    def start_app(self):
        pyautogui.sleep(2)
        pyautogui.hotkey('win', 'down')
        pyautogui.hotkey('win', 'down')
        pyautogui.sleep(2)

        try:
            pyautogui.doubleClick(self.X, self.Y)
            print(f"Clicked on screen at ({self.X}, {self.Y}) successfully!")
        except Exception as e:
            return f"Error while clicking on screen: {e}"
