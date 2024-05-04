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

from rich.console import Console
from typing import Generator

def save(data: Generator) -> str:
    """Save data in a json."""
    format_data = {}
    count = 0
    choiced = False
    # iterate through the generator and distinguish elements
    for val in data[0]:
        if len(val) == 2:
            format_data[f"point{count}"] = val
            count += 1
        else:
            if choiced:
                format_data[f"choice2"] = val
            else:
                format_data[f"choice1"] = val
                choiced = True
    format_data["total_time"] = data[1]
    # construct file name
    file_name = "data/"
    date = datetime.datetime.now()
    file_name += date.strftime("%Y-%d-%m-%H-%M-%S") + ".json"
    # write to file
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(format_data, file, ensure_ascii=False, indent=4)
    # return file name
    return file_name

def display(file_name: str):
    """Take in a json file and display the data in a readable manner."""
    # define a console for printing
    console = Console()
    # get the data
    with open(file_name) as json_data:
        data = json.load(json_data)
    console.print("Overall:")
    console.print(f"\tPlayer was on the page for {data['total_time']} seconds.")
    console.print("\nQuestion 1:")
    console.print(f"\tPlayer's mouse traveled {data['choice1'][2]} from the start point.")
    console.print(f"\tPlayer's response to {data['choice1'][0]} was {data['choice1'][1]}.")
    console.print("\nQuestion 2:")
    console.print(f"\tPlayer's mouse traveled {data['choice2'][2]} from the start point.")
    console.print(f"\tPlayer's response to {data['choice2'][0]} was {data['choice2'][1]}.")