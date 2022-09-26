from dataclasses import dataclass
from typing import List
import json


@dataclass
class ServerConfig:
    HOST_IPV4: str
    HOST_PORT: int
    SEPARATOR: str


def read_config(config_file: str) -> ServerConfig:
    with open(config_file, 'r') as file_in:
        data = json.load(file_in)
        return ServerConfig(**data)
