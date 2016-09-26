import sys
import os
import time
import subprocess

pwdPath = str(os.getcwd()) + "/"
fileToConvert = str(sys.argv[1])

subprocess.call("pdftotext " + pwdPath + fileToConvert + ".pdf", shell=True)

with open(fileToConvert + ".txt", "r") as file:
    draft = file.read()
    print draft

