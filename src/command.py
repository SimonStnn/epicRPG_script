import time
import pyautogui

from const import CONFIG


class Command:
    def __init__(
        self, cmd: str, delay: float, heal_interval: int | None = None
    ) -> None:
        self.cmd = cmd
        self.delay = delay + 0.8  # Add bit of extra delay to account for delay to bot
        self.heal_interval = heal_interval

        self.last_executed = 0
        self.now = 0

        self.counter = 0

    @property
    def should_execute(self) -> bool:
        self.now = time.time()
        if self.now - self.last_executed > self.delay:
            self.last_executed = self.now
            return True
        return False

    def execute(self):
        self.counter += 1

        if self.heal_interval:
            if self.counter % self.heal_interval == 0:
                self._run_command("/heal")
            else:
                print(
                    "\tHealing in "
                    + str(self.heal_interval - (self.counter % self.heal_interval))
                    + " commands"
                )

        self._run_command(self.cmd)

    def _run_command(self, command: str):
        print("\tRunning command: " + command)
        pyautogui.typewrite(command, interval=CONFIG["type-interval"])
        time.sleep(0.25)
        pyautogui.typewrite("\t\n\n\n", interval=CONFIG["type-interval"] * 3)
        time.sleep(0.1)