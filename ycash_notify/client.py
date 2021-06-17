import time
import subprocess
import json
import base64
import os
import sys

z_listunspent = "./z_listunspent.sh"
payload = json.loads(subprocess.check_output(z_listunspent, shell=True).strip())
print(payload)
