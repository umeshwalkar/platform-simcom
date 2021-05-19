# 
##########################################################################
# Autor: Umesh Walkar 2021
#   http://www.beyondlogics.in/
#   https://github.com/umeshwalkar/platform-simcom
# 
# Support: Comet Electronics 
#   https://www.comet.bg/?cid=92
##########################################################################

from os.path import join
from SCons.Script import (AlwaysBuild, Builder, COMMAND_LINE_TARGETS, Default, DefaultEnvironment)
from colorama import Fore

env = DefaultEnvironment()
print( Fore.GREEN + '<<<<<<<<<<<< '+env.BoardConfig().get("name").upper()+" 2021 Umesh Walkar >>>>>>>>>>>>" )

####################################################
# Build executable and linkable program
####################################################
elf = env.BuildProgram()
src = env.MakeHeader( join("$BUILD_DIR", "${PROGNAME}"), env.ElfToBin(join("$BUILD_DIR", "${PROGNAME}"), elf) )
AlwaysBuild( src )

upload = env.Alias("upload", src, [ 
    env.VerboseAction(env.AutodetectUploadPort, "Looking for upload port..."),
    env.VerboseAction("$UPLOADCMD", '\033[93m'+"Uploading: $PROGNAME"),
    env.VerboseAction("", '\033[93m'+"Ready"),
])
AlwaysBuild( upload )    

Default( src )
