import os
import subprocess
import time
import json

# load the configuration file

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

#load variables from config file
directory = config["repo_location"]
sleep_time = config["sleep"]

#execute updater
os.chdir(directory)
while True:
    subprocess.call(["git", "pull", "origin", "master"])
    time.sleep(5)
