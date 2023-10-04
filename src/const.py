import yaml
from typing import Final, Any

def _load_config():
    with open("config.yaml", "r") as yaml_file:
        config: dict[str, Any] = yaml.safe_load(yaml_file)
    return config

CONFIG: Final = _load_config()