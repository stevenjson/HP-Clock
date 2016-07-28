import time
import subprocess

process = subprocess.Popen("tail -n 1 data/output", stdout=subprocess.PIPE)
output = process.communicate()[0]
print (output)
