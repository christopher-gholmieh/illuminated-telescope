# Written by: Christopher Gholmieh
# Imports:

# Dataclasses:
from dataclasses import dataclass, field

# Node:
from .node import Node


# Node:
@dataclass
class Document:
    # Architecure:
    # Nodes:
    nodes: list[Node] = field(default_factory=list)
