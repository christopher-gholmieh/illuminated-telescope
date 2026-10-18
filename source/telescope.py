# Written by: Christopher Gholmieh
# Imports:

# Subprocess:
import subprocess


# Telescope:
class Telescope:
    # Initialization:
    def __init__(self) -> None:
        pass

    # Methods:
    def is_package_installed(self, package: str) -> bool:
        try:
            subprocess.run(
                # Arguments:
                ["dpkg-query", "-W", "-f=${Status}", package],
                
                # Output:
                stdout=subprocess.PIPE,

                # Error:
                stderr=subprocess.PIPE,

                # Text:
                text=True,

                # Check:
                check=True,
            )

            return True
        except subprocess.CalledProcessError:
            return False
