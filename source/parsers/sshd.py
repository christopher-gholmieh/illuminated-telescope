# Written by: Christopher Gholmieh
# Imports:

# Structure:
from .structure import Document, Node

# Pathlib:
from pathlib import Path

# Loguru:
from loguru import logger


# Parser:
class SSHDParser:
    """
    There haven't been any match statements in CyberPatriots before; hence, this parser assumes
    that all match statements can be ignored and are at the end of the file, in accordance with
    SSH configuration syntax.
    """

    # Initialization:
    def __init__(self) -> None:
        # Variables (Assignment):
        # Directories:
        self.directories: list[str] = ["/etc/ssh/sshd_config.d/"]

        # Files:
        self.files: list[str] = ["/etc/ssh/sshd_config"]

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

        # Directories:
        for directory in self.directories:
            # Variables (Assignment):
            # Path:
            path: Path = Path(directory)

            # Files:
            files: list[str] = [str(file) for file in path.rglob("*") if file.is_file()]

            # Logic:
            for file_path in files:
                self.iterate(document, file_path)

        # Files:
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

        # Logic:
        with open(file_path, "r", encoding="utf-8") as configuration_file:
            # Variables (Assignment):
            # Lines:
            lines: list[str] = configuration_file.readlines()

            # Logic:
            for number, raw_line in enumerate(lines, start=1):
                # Variables (Assignment):
                # Line:
                line: str = raw_line.strip()

                # Clause:
                if not line or line.startswith("#"):
                    continue

                # Logic:
                if line.casefold().startswith("match"):
                    # Loguru:
                    logger.warning(
                        f"[*] [{file_path}:{number}]: The SSHD parser has encountered conditional match statements that won't be checked."
                    )

                    # Logic:
                    break
                else:
                    # Variables (Assignment):
                    # Content:
                    content: list[str] = line.split()

                    # Term:
                    term: str = content[0]

                    document.nodes.append(
                        Node(
                            # Arguments:
                            arguments=content[1::],

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
                            group_owner=path.group(),

                            # User:
                            user_owner=path.owner(),

                            # Access:
                            access=self.get_octal_permissions(path),
                        )
                    )
