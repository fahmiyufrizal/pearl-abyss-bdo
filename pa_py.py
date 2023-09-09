# pearl-abyss-bdo simple launcher
# by fahmiyufrizal@2023

import os
import subprocess
from os import path
from sys import exit
import asyncio
import pathlib

# parameters
version = 'v1.0'
titlewindow = 'fahmiyufrizal@2023 [github.com/fahmiyufrizal]'
PAFN = (r'PearlAbyss_BDO_Launcher.exe')
PAMLN = (r'_Data_\Local\Pearl-Abyss-Launcher\Pearl Abyss Launcher.exe')
dp0 = os.getcwd()
local_PA = path.expandvars(r'%localappdata%\Pearl-Abyss-Launcher')
appdata_PA = path.expandvars(r'%appdata%\Pearl Abyss Launcher')
local_PA_config = (r'_Data_\Local\Pearl-Abyss-Launcher')
appdata_PA_config = (r'_Data_\Roaming\Pearl Abyss Launcher')
 # damn