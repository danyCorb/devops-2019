import json
import subprocess


# Run it un /script dir ("console")

with open("automate.json") as automateConfigFile:  
    automatConfig = json.load(automateConfigFile)
for automate in automatConfig:
    subprocess.Popen(["python", "automate/generator.py", automate["id"], automate["port"]])
    print(automate["ip"]+":"+automate["port"])