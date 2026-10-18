# Written by: Christopher Gholmieh
# Imports:

# Parsers:
from .parsers import PostfixParser, SSHDParser, Document

# Typing:
from typing import Any


# Extractor:
class Extractor:
    # Initialization:
    def __init__(self) -> None:
        # Variables (Assignment):
        # Parsers:
        self.parser_map: dict[str, Any] = {
            # Postfix:
            "postfix": PostfixParser(),

            # SSHD:
            "openssh-server": SSHDParser(),
        }

    # Methods:
    def extract(self, installed_services: list[str]) -> dict[str, Document]:
        # Variables (Assignment):
        # Map:
        map: dict[str, Document] = {}

        # Logic:
        for installed_service in installed_services:
            map[installed_service] = self.parser_map[installed_service].parse()

        # Map:
        return map
