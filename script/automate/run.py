import json
import subprocess



with open("automate.json") as automateConfigFile:  
    automatConfig = json.load(automateConfigFile)
for automate in automatConfig:
    subprocess.Popen(["python", "generator.py", automate["id"], automate["port"]])
    print(automate["ip"]+":"+automate["port"])