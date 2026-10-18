# Written by: Christopher Gholmieh
# Imports:

# Future:
from __future__ import annotations

# Dataclasses:
from dataclasses import dataclass, field

# Typing:
from typing import Literal


# Node:
@dataclass
class Node:
    # Attributes:
    # Arguments:
    arguments: list[str]

    # Kind:
    kind: Literal["Directive", "Scope"]

    # Name:
    name: str

    # Metadata:
    # File:
    file: str

    # Line:
    line: int

    # Filesystem:
    # Group:
    group_owner: str

    # User:
    user_owner: str

    # Access:
    access: str

    # Architecture:
    # Children:
    children: list[Node] = field(default_factory=list)
