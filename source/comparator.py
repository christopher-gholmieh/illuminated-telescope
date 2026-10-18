# Written by: Christopher Gholmieh
# Imports:

# Telescope:
from .telescope import Telescope

# Extractor:
from .extractor import Extractor


# Comparator:
class Comparator:
    # Initialization:
    def __init__(self) -> None:
        # Variables (Assignment):
        # Telescope:
        self.telescope: Telescope = Telescope()

        # Extractor:
        self.extractor: Extractor = Extractor()

    # Methods:
    def compare(self) -> None:
        pass
