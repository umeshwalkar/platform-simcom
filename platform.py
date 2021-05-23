# 2021 Umesh Walkar
#   http://www.beyondlogics.in/
#   https://github.com/umeshwalkar/platform-simcom

from platform import system
from platformio.managers.platform import PlatformBase

class SimcomPlatform(PlatformBase):
    def configure_default_packages(self, variables, targets):
#        framework = variables.get("pioframework", [])
#        if variables["board"].startswith('ec2'):
#            del self.packages["toolchain-gccarmnoneeabi"]
#        else:
#            del self.packages["toolchain-gcc-ec2x"]
        return PlatformBase.configure_default_packages(self, variables, targets)