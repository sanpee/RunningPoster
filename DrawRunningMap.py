from pathlib import Path
import os
import json
import matplotlib.pyplot as plt
from fit_tool.fit_file import FitFile
from fit_tool.profile.messages.record_message import RecordMessage

def main():

    actitivy_directory = Path.home().joinpath('HealthData/FitFiles/Activities')
    for file in os.scandir(actitivy_directory):
        if file.is_file():
            if ".json" in file.path:
                with open(file.path) as json_file:
                    activity = json.load(json_file)     
                    
                    fit_filepath = file.path.replace(".json", ".fit")
                    print(fit_filepath)

    return

    app_fit = FitFile.from_file(Path.home().joinpath('HealthData/FitFiles/Activities', '7764267098_ACTIVITY.fit'))
    app_fit.to_csv('7764267098_ACTIVITY.csv')
    timestamp1 = []
    power1 = []
    distance1 = []
    speed1 = []
    cadence1 = []
    pos_long = []
    pos_lat = []
    for record in app_fit.records:
        message = record.message
        if isinstance(message, RecordMessage):
            timestamp1.append(message.timestamp)
            distance1.append(message.distance)
            power1.append(message.power)
            speed1.append(message.speed)
            cadence1.append(message.cadence)
        elif isinstance(message, CourseMessage):    
            pos_long.append(message.position_long)
            pos_lat.append(message.position_lat)

    # plt.scatter(x=pos_lat[101:1000], y=pos_long[101:1000])
    plt.scatter(x=pos_lat, y=pos_long)
    # plt.plot(pos_long)
    plt.show()



if __name__ == "__main__":
    main()