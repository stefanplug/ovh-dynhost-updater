import json
import os


def load_json(relative_file_location):
    """Loads a JSON into a dict and handles the exceptions
    Parameters:
    relative_file_location (str): relative from this json_functions file
    Returns:
    config (dict): The JSON in dict form"""
    relative_file_location = "../{0}".format(relative_file_location)
    file_location = os.path.join(os.path.dirname(__file__), relative_file_location)
    if not (os.path.exists(file_location) and os.path.isfile(file_location)):
        msg = "Missing or invalid config file {0}".format(file_location)
        raise ValueError(msg)
    try:
        with open(file_location, 'r') as file:
            data = json.load(file)
    except Exception as err:
        print(err)
        exit()
    return data


def export_json(data, relative_file_location):
    """exports a dict into a JSON and handles the exceptions
    Parameters:
    relative_file_location (str): relative from this json_functions file
    Returns:
    config (dict): The JSON in dict form"""
    relative_file_location = "../{0}".format(relative_file_location)
    file_location = os.path.join(os.path.dirname(__file__), relative_file_location)
    #if not (os.path.exists(file_location) and os.path.isfile(file_location)):
    #    msg = "Missing or invalid config file {0}".format(file_location)
    #    raise ValueError(msg)
    try:
        with open(file_location, 'w+') as file:
            data = json.dump(data, file, indent=2)
    except Exception as err:
        print(err)
        exit()
