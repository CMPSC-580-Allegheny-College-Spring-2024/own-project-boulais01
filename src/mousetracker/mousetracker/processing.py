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

def save(data):
    """Save data in a json."""
    format_data = []
    count = 0
    for val in data:
        if len(val) == 2:
            format_data.append({f"point{count}": val})
            count += 1
        else:
            format_data.append({f"choice": val})
    file_name = "data/"
    date = datetime.date.today()
    time = datetime.time()
    file_name += date.isoformat() + time.strftime("HH-MM-SS") + ".json"
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(format_data, file, ensure_ascii=False, indent=4)