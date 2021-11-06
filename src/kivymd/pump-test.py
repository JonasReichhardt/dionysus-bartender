from src.kivymd.Model.Pump import *
from pathlib import Path

config_file = RES_PATH = Path("../res/pump-config.json")
millilitres = [30,60,90,120,150]

provider = PumpFactory(str(config_file))
pumps = provider.loadFromFile()

def calibrate(pump):
    for milli in millilitres:
        while True:
            print("Target quantity "+str(milli)+"ml")
            pump.activate_blocking(milli)
            user_input = input("Result correct?")
            print("\n")
            if user_input == 'y':
                break
    return False


print("Starting calibration...")

for pump in pumps:
    uncalibrated = True
    print("\n")
    print("Calibrating",pump.ingredient)
    while uncalibrated:
        uncalibrated = calibrate(pump)
