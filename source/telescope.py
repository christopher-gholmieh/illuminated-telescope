# Written by: Christopher Gholmieh
# Imports:

# Subprocess:
import subprocess


# Telescope:
class Telescope:
    # Initialization:
    def __init__(self) -> None:
        # Variables (Assignment):
        # Services:
        self.critical_services: list[str] = [
            "openssh-server"
        ]

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

    def scope(self) -> list[str]:
        # Variables (Assignment):
        # Services:
        services: list[str] = [
            service for service in self.critical_services
                if self.is_package_installed(service)
        ]

        # Services:
        return services
