# Written by: Christopher Gholmieh
# Imports:

# Structure:
from .structure import Document, Node

# Pathlib:
from pathlib import Path

# Loguru:
from loguru import logger


# Parser:
class PostfixParser:
    # Initialization:
    def __init__(self) -> None:
        # Variables (Assignment):
        # Files:
        self.files: list[str] = ["/etc/postfix/main.cf"]

    # Methods:
    def get_octal_permissions(self, path: Path) -> str:
        # Variables (Assignment):
        # Mode:
        mode: int = path.stat().st_mode

        # Logic:
        return f"{mode & 0o777:o}"

    def parse(self) -> Document:
        # Variables (Assignment):
        # Document:
        document: Document = Document()

        for file_path in self.files:
            self.iterate(document, file_path)

        # Document:
        return document

    def iterate(self, document: Document, file_path: str) -> None:
        # Variables (Assignment):
        # Path:
        path: Path = Path(file_path)

        # Validation:
        if not path.exists():
            return

        # Metadata:
        # Group:
        group_owner: str = path.group()

        # User:
        user_owner: str = path.owner()

        # Access:
        access: str = self.get_octal_permissions(path)


        # Node:
        current_node: Node | None = None

        # Logic:
        with open(file_path, "r", encoding="utf-8") as configuration_file:
            # Logic:
            for number, raw_line in enumerate(configuration_file, start=1):
                # Variables (Assignment):
                # Line:
                line: str = raw_line.strip()

                # Clause:
                if not line or line.startswith("#"):
                    continue

                if raw_line[0].isspace():
                    # Validation:
                    if current_node is None:
                        # Loguru:
                        logger.warning(f"[!] [{file_path}:{number}]: Continuation line without a preceding directive!")

                        # Logic:
                        continue

                    # Variables (Assignment):
                    # Previous:
                    previous_value: str = current_node.arguments[0]

                    # Node:
                    current_node.arguments[0] = f"{previous_value} {line}" if previous_value else line

                    # Logic:
                    continue
                else:
                    # Variables (Assignment):
                    # Node:
                    current_node = None

                # Validation:
                if not "=" in line:
                    # Loguru:
                    logger.warning(f"[*] [{file_path}:{number}]: Invalid Postfix syntax; expected key = value")

                    # Logic:
                    continue

                # Variables (Assignment):
                # Term & Value:
                term, value = line.split("=", 1)

                # Processing:
                term = term.strip()
                value = value.strip()

                # Validation:
                if not term:
                    # Loguru:
                    logger.warning(f"[*] [{file_path}:{number}]: Invalid Postfix syntax; invalid parameter name!")

                    # Logic:
                    continue

                # Node:
                current_node = Node(
                    # Arguments:
                    arguments=[value],

                    # Kind:
                    kind="Directive",

                    # Name:
                    name=term,

                    # File:
                    file=file_path,

                    # Line:
                    line=number,

                    # Children:
                    children=[],

                    # Group:
                    group_owner=group_owner,

                    # User:
                    user_owner=user_owner,

                    # Access:
                    access=access
                )

                # Logic:
                document.nodes.append(current_node)
