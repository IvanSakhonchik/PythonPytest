import time

import pyautogui

from framework.utilities.config_manager import image_path


class EmulatorUtils:
    @staticmethod
    def input_image():
        time.sleep(2)
        pyautogui.write(image_path)
        pyautogui.press('enter')
        time.sleep(2)
