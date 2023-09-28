import time
import pyautogui

MOVE_DURATION = 0.3
TYPE_INTERVAL = 0.1


class Command:
    def __init__(self, cmd: str, delay: int, heal_interval: int | None = None) -> None:
        self.cmd = cmd
        self.delay = delay
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
        # return
        pyautogui.typewrite(command, interval=TYPE_INTERVAL)
        pyautogui.typewrite("\t\n\n", interval=TYPE_INTERVAL)
        # pyautogui.press("enter")
        time.sleep(0.1)


class Script:
    commands: list[Command] = []

    def __init__(self) -> None:
        pass

    def run(self):
        self.click(1900, 2100)
        time.sleep(5)
        while True:
            print("loop")
            for command in self.commands:
                if command.should_execute:
                    command.execute()
            time.sleep(0.5)

    def click(self, x: int, y: int):
        pyautogui.moveTo(x, y, duration=MOVE_DURATION)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.1)

    def register(self, command: str, delay: int, *, heal_inteval: int = None):
        self.commands.append(Command(command, delay, heal_inteval))


if __name__ == "__main__":
    script = Script()
    # Run /hunt every 60 seconds, and every 10 times do a /heal
    script.register("/hunt", 1 * 60, heal_inteval=10)
    # Run /adventure every 60 minutes
    script.register("/adventure", 60 * 60)
    # RUn /farm every 10 minutes
    script.register("/farm", 10 * 60)

    print("Script started, press CTRL+C to stop")
    try:
        script.run()
    except KeyboardInterrupt:
        print("Script stopped, Bye!")
