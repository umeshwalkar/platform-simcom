
# 2021 Umesh Walkar
#   http://www.beyondlogics.in/
#   https://github.com/umeshwalkar/platform-simcom

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()
platform = "embeddedat"
module = platform + "-" + env.BoardConfig().get("build.core")
m = __import__(module)       
globals()[module] = m
m.dev_init(env, platform)
print( env.Dump() )






