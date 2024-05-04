"""Process output from the game and tracker."""

# iterate through generator(s), count how many results;
# use in dividing time to assess length of time at each point;
# e.g. time / num_points and however many points are constant;
# user remained at point.

# take question data and add to json as well;
# create a file if it doesn't exist, otherwise;
# add to existing file? or make new file for each run;
# named using date and time. 

import json
import datetime

from typing import Generator

def save(data: Generator) -> str:
    """Save data in a json."""
    format_data = []
    count = 0
    for val in data[0]:
        if len(val) == 2:
            format_data.append({f"point{count}": val})
            count += 1
        else:
            format_data.append({f"choice": val})
    format_data.append({"total_time": data[1]})
    file_name = "data/"
    date = datetime.datetime.now()
    file_name += date.strftime("%Y-%d-%m-%H-%M-%S") + ".json"
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(format_data, file, ensure_ascii=False, indent=4)
    return file_name

def display(file_name: str):
    """Take in a json file and display the data in a readable manner."""
    with open(file_name) as json_data:
        data = json.load(json_data)
    