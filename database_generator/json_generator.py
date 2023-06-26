
import json
from datetime import datetime
from components.database_formatter import format_special_char

activity_database = {}

def add_item_to_database(activity_name:str, activity_values:str):
    activity_database[activity_name] = activity_values
    
def generate_json(start_year, end_year):

    current_time = datetime.now().strftime('%H:%M:%S')
    file_name = "extension_activity_database_" + str(start_year) + str(end_year) + str(current_time)
    file_output = open(file_name, "w")
    json.dump(activity_database, file_output, indent=3)
    format_special_char(file_name)
