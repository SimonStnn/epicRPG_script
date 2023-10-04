import time
import pyautogui

from script import Script
from const import CONFIG

if __name__ == "__main__":
    script = Script()

    commands: dict[str, float | dict[str, float | int]] = CONFIG["commands"]
    for cmd, data in commands.items():
        if isinstance(data, dict):
            delay = data["delay"]
            heal_interval: int | None = (
                int(data["heal-interval"]) if "heal-interval" in data else None
            )
        else:
            delay = data
            heal_interval = None
        script.register(
            cmd, delay * 60, heal_inteval=heal_interval
        )  # Convert minutes to seconds

    # Open discord
    pyautogui.press("win")
    time.sleep(1)
    pyautogui.typewrite("discord", interval=CONFIG["type-interval"])
    time.sleep(1)
    pyautogui.press("enter")

    print("Script started, press CTRL+C to stop")
    try:
        script.run()
    except KeyboardInterrupt:
        print("Script stopped, Bye!")
