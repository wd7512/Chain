import os
from sys import platform
if platform == 'win32': #Windows
  os.system('python -m pip install venv')
else: #macos
