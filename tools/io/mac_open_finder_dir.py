import subprocess
import os
path = os.getcwd()
if os.path.exists(path):
    subprocess.call(["open", "-R", path])