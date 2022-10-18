# ------------------------------------------------------------------------------------------------------
# os Python module
# ------------------------------------------------------------------------------------------------------

# os connects Python with System OS
import os

# system() allows to execute OS commands in a rusty way
os.system("ls")
if not os.path.exists("./newFolder"):
    os.mkdir("newFolder")

if os.path.exists("./newFolder"):
    os.rmdir("newFolder")


# subprocess better executing commands
import subprocess

subprocess.call(["ls", "-la"])

subprocess.call("date")
