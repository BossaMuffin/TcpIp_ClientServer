from dataclasses import dataclass
from typing import List
import json


@dataclass
class ClientConfig:
    HOST_IPV4: str
    HOST_PORT: int
    MESSAGES_LIST: List[str]
    ATTEMPTS_BUFFER: int
    ATTEMPTS_LIMIT: int
    SEPARATOR: str


def read(config_file: str) -> ClientConfig:
    with open(config_file, 'r') as file_in:
        data = json.load(file_in)
        return ClientConfig(**data)
