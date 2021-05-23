# 2021 Umesh Walkar
#   http://www.beyondlogics.in/
#   https://github.com/umeshwalkar/platform-simcom

import os
from os.path import join
from shutil import copyfile
from SCons.Script import ARGUMENTS, DefaultEnvironment, Builder
#from mc60 import makeHDR, makeCFG
#from MT6261 import upload_app

#def dev_uploader(target, source, env):
#    return upload_app(env.BoardConfig().get("build.core"), join(env.get("BUILD_DIR"), "program.bin"), env.get("UPLOAD_PORT")) 

#def dev_header(target, source, env):
#    makeHDR( source[0].path )
#    makeCFG( source[0].path )

def dev_create_template(env):
    D = join(env.subst("$PROJECT_DIR"), "build")
    if False == os.path.isdir(D): 
        os.makedirs(D)
    
        S = join(env.PioPlatform().get_package_dir("framework-simcom"), "templates", env.BoardConfig().get("build.core"), "build")
        F = [
            "app_build.mak",
            "Makefile",
            "option.mak",
            "user.mak",                                           
        ]
        for I in F:
            dst = join(D, I)
            if False == os.path.isfile(dst): 
                copyfile(join(S, I), dst) 
    
    D1 = join(env.subst("$PROJECT_DIR"), "build", "winmake")
    if False == os.path.isdir(D1): 
        os.makedirs(D1)
            
        S = join(env.PioPlatform().get_package_dir("framework-simcom"), "templates", env.BoardConfig().get("build.core"), "build", "winmake")
        F = [
            "appgen.exe",
            "cmp.exe",
            "cp.exe",
            "diff.exe",
            "gdate.exe",
            "gecho.exe",
            "ginstall.exe",
            "grep.exe",  
            "make.exe",
            "mv.exe",
            "patch.exe",
            "pwd.exe",                                             
            "rm.exe",
            "upx.exe",
            "zip.exe",
        ]
        for I in F:
            dst = join(D1, I)
            if False == os.path.isfile(dst): 
                copyfile(join(S, I), dst) 

    #return
    #copy main.c if file not exist
    D = join(env.subst("$PROJECT_DIR"), "src")
    if False == os.path.isdir(D): 
        os.makedirs(D)

    D1 = join(env.subst("$PROJECT_DIR"), "src", "application")
    if False == os.path.isdir(D1): 
        os.makedirs(D1)
        S = join(env.PioPlatform().get_package_dir("framework-simcom"), "templates", env.BoardConfig().get("build.core"), "src", "app")
        F = [
            "main.c",
            "makefile",                                                     
        ]
        for I in F:
            dst = join(D1, I)
            if False == os.path.isfile(dst): 
                copyfile(join(S, I), dst) 
    
    #copy SIM868M32.bat if file not exist
    S = join(env.PioPlatform().get_package_dir("framework-simcom"), "templates", env.BoardConfig().get("build.core"))
    if False == os.path.isfile( join(env.subst("$PROJECT_DIR"), "SIM868M32.bat") ):
        copyfile( join(S, "SIM868M32.bat"), join(env.subst("$PROJECT_DIR"), "SIM868M32.bat") )                    	

    #copy "core" files
    D = join(env.subst("$PROJECT_DIR"), "core")
    if False == os.path.isdir(D): 
        os.makedirs(D)    
        S = join(env.PioPlatform().get_package_dir("framework-simcom"), "templates", env.BoardConfig().get("build.core"), "core")
        F = [
            "core.lib",
            "SIM868M32_EAT.cfg",
            "scat_SIM868M32.txt",                                              
        ]
        for I in F:
            dst = join(D, I)
            if False == os.path.isfile(dst): 
                copyfile(join(S, I), dst) 
 
    #copy "core->inc" files
    D1 = join(env.subst("$PROJECT_DIR"), "core", "inc")
    if False == os.path.isdir(D1): 
        os.makedirs(D1)
        S = join(env.PioPlatform().get_package_dir("framework-simcom"), "templates", env.BoardConfig().get("build.core"), "core", "inc")
        F = [
            "app_interface.h",
            "eat_audio.h",
            "eat_clib_define.h", 
            "eat_flash.h", 
            "eat_fs.h", 
            "eat_fs_errcode.h", 
            "eat_fs_type.h", 
            "eat_gps.h", 
            "eat_interface.h", 
            "eat_mem.h", 
            "eat_modem.h", 
            "eat_network.h", 
            "eat_nvram.h", 
            "eat_other.h", 
            "eat_periphery.h", 
            "eat_sim.h", 
            "eat_soft_sim.h", 
            "eat_timer.h", 
            "eat_type.h", 
            "eat_uart.h", 
        ]
        for I in F:
            dst = join(D1, I)
            if False == os.path.isfile(dst): 
                copyfile(join(S, I), dst) 

    #copy "core->SIM868M32_EMBEDDEDAT" files
    D1 = join(env.subst("$PROJECT_DIR"), "core", "SIM868M32_EMBEDDEDAT")
    if False == os.path.isdir(D1): 
        os.makedirs(D1)
        S = join(env.PioPlatform().get_package_dir("framework-simcom"), "templates", env.BoardConfig().get("build.core"), "core", "SIM868M32_EMBEDDEDAT")
        F = [
            "1418B01SIM868M32_EAT.cfg",
            "app",                                                     
            "appnull",
            "BPLGUInfoCustomAppSrcP_MT6261_S00_1418B01SIM868M32_EAT",
            "COREAPI",
            "EXT_BOOTLOADER",
            "ROM",
            "ROM_VIVA",
            "SIM868M32_EAT.cfg",
            "SIM868M32_EAT_BOOTLOADER.bin",
            "SIM868M32_EAT_core_only.cfg",
            "SIM868M32_EAT_PCB01_gprs_MT6261_S00.elf",
            "SIM868M32_EAT_PCB01_gprs_MT6261_S00.sym",
            "SIM868M32_EAT_PCB01_gprs_MT6261_S00_limit.sym",
            "VIVA",
        ]
        for I in F:
            dst = join(D1, I)
            if False == os.path.isfile(dst): 
                copyfile(join(S, I), dst)  

#def dev_compiler(env):
#    env.Replace(
#        BUILD_DIR = env.subst("$BUILD_DIR").replace("\\", "/"),
#        AR="arm-none-eabi-ar",
#        AS="arm-none-eabi-as",
#        CC="arm-none-eabi-gcc",
#        GDB="arm-none-eabi-gdb",
#        CXX="arm-none-eabi-g++",
#        OBJCOPY="arm-none-eabi-objcopy",
#        RANLIB="arm-none-eabi-ranlib",
#        SIZETOOL="arm-none-eabi-size",
#        ARFLAGS=["rc"],
#        SIZEPROGREGEXP=r"^(?:\.text|\.data|\.bootloader)\s+(\d+).*",
#        SIZEDATAREGEXP=r"^(?:\.data|\.bss|\.noinit)\s+(\d+).*",
#        SIZECHECKCMD="$SIZETOOL -A -d $SOURCES",
#        SIZEPRINTCMD='$SIZETOOL --mcu=$BOARD_MCU -C -d $SOURCES',
#        PROGSUFFIX=".elf",  
#    )

def dev_init(env, platform):
    dev_create_template(env)
#    dev_compiler(env)
    framework_dir = env.PioPlatform().get_package_dir("framework-simcom")
    core = env.BoardConfig().get("build.core")     
    variant = env.BoardConfig().get("build.variant")  
    #lib_dir = join(framework_dir, "libraries")
    #linker = join(lib_dir, "c_{}.ld".format(core))
    env.firmware = env.BoardConfig().get("build.firmware", "").replace("-", "_").replace(".", "_").upper()   
    env.Append(
       CPPDEFINES = [ # -D                         
            platform.upper(), "CORE_" + core.upper().replace("-", "_"),            
        ],        
        CPPPATH = [ # -I
        #    join(framework_dir, platform, core),
        #    join(framework_dir, platform, core, "include"),
        #    join(framework_dir, platform, core, "ril", "inc"),
        #    join(framework_dir, platform, core, "fota", "inc"),
        #    join(framework_dir, platform, core, "cloud", "http", "inc"),
        #    join(framework_dir, platform, core, "cloud", "protocol", "mqtt", "inc"),
        #    join(framework_dir, platform, core, "cloud", "entity", "gitwizs", "inc"),                        
            join("$PROJECT_DIR", "core"),
            join("$PROJECT_DIR", "output"), 
            join("$PROJECT_DIR", "src"), 
            join("$PROJECT_DIR", "build")
        ],        
        #CFLAGS = [
        #    "-Os",
        #    "-march=armv5te",
        #    "-mfloat-abi=soft",
        #    "-mfpu=vfp",
        #    "-mthumb",
        #    "-mthumb-interwork",  
        #    "-std=c11",             
        #    "-fno-builtin",
        #    "-fno-strict-aliasing",            
        #    "-fsingle-precision-constant",                                     
        #    "-Wall",            
        #    "-Wstrict-prototypes",
        #    "-Wp,-w",                
        #],        
        #LINKFLAGS = [    
        #    "-march=armv5te",
        #    "-mfloat-abi=soft",
        #    "-mfpu=vfp",
        #    "-mthumb",
        #    "-mthumb-interwork",   
        #    "-nostartfiles",            
        #    "-Wl,--gc-sections,--relax", 
        #],    
        #LIBPATH = [ lib_dir ],      
        #LDSCRIPT_PATH = linker, 
        #LIBS = [ "gcc","m","_app_start_{}".format(core) ],               
        #BUILDERS = dict(
        #    ElfToBin = Builder(
        #        action = env.VerboseAction(" ".join([
        #            "$OBJCOPY",
        #            "-O",
        #            "binary",
        #            "$SOURCES",
        #            "$TARGET",
        #        ]), "Building $TARGET"),
        #        suffix = ".dat"
        #    ),    
        #    MakeHeader = Builder( 
        #        action = env.VerboseAction(dev_header, "ADD HEADER"),
        #        suffix = ".bin"
        #    )       
        #), 
        #UPLOADCMD = dev_uploader
    )
    #libs = []      
    #libs.append(
    #    env.BuildLibrary(
    #        join("$BUILD_DIR", "_opencpu"),
    #        join(framework_dir, platform, core),
    #))  
    #libs.append(
    #    env.BuildLibrary(
    #        join("$BUILD_DIR", "_custom_lib"), 
    #        join("$PROJECT_DIR", "lib"),                       
    #))         
    #libs.append(
    #    env.BuildLibrary(
    #        join("$BUILD_DIR", "_custom_config"), 
    #        join("$PROJECT_DIR", "config"),                       
    #))   
    
    #if env.firmware != "":
    #    env.Append(
    #        CPPPATH = [join(framework_dir,  "api", core)],              
    #        LIBS = ["_{}".format(env.firmware)]
    #    )
    #    libs.append(
    #        env.BuildLibrary(
    #            join("$BUILD_DIR", "_api"),
    #            join(framework_dir, "api", core),
    #    ))  

    #env.Append(LIBS = libs)   