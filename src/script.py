import time
import pyautogui

from command import Command
from const import CONFIG


class Script:
    commands: list[Command] = []

    def __init__(self) -> None:
        pass

    def run(self):
        time.sleep(3)
        while True:
            for command in self.commands:
                if command.should_execute:
                    command.execute()
            time.sleep(0.5)

    def click(self, x: int, y: int):
        pyautogui.moveTo(x, y, duration=CONFIG["mouse-duration"])
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.1)

    def register(self, command: str, delay: float, *, heal_inteval: int | None = None):
        self.commands.append(Command(command, delay, heal_inteval))
