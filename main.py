# Written by: Christopher Gholmieh
# Imports:

# Source:
from source import Comparator

# Platform:
import platform

# Loguru:
from loguru import logger


# Platform:
if not platform.system() == "Linux":
    # Loguru:
    logger.error("[!] The illuminated-telescope project only works on Linux systems!")

    # Logic:
    exit()


# Variables (Assignment):
# Comparator:
comparator: Comparator = Comparator()

# Logic:
comparator.compare()