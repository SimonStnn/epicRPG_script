import time
import pyautogui
from typing import Any

from script import Script
from command import Command
from const import CONFIG

if __name__ == "__main__":
    script = Script()

    commands: dict[str, Any | dict[str, Any]] = CONFIG["commands"]
    for cmd, data in commands.items():
        if not isinstance(data, dict):
            data = {"delay": data}

        delay = float(data["delay"]) * 60  # Convert minutes to seconds
        heal_interval = int(data["heal-interval"]) if "heal-interval" in data else None
        args = dict(data["args"]) if "args" in data else {}
        args_auto_selected = (
            data["args-auto-selected"] if "args-auto-selected" in data else False
        )
        
        script.register(
            Command(
                cmd,
                delay,
                heal_interval,
                args,
                args_auto_selected,
            )
        )

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
