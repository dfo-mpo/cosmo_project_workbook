import word_dictionary as wd
import os  
import glob  
import json  
import ast  
import pandas as pd  
  
# Function to convert string representation of list to actual list  
def convert_to_list(cell):  
    try:  
        return ast.literal_eval(cell)  
    except (ValueError, SyntaxError):  
        # Return the cell as-is if it's not a string representation of a list  
        return cell  
  
# Function to update the list based on the content and confidence of a value, assumes that if polygon exists it is the secent entry in the value
# This assignment of 1 or 0 determines if human review is needed for the given entry
def update_list(value):
    valSize = len(value)
    if isinstance(value, list) and valSize in [2,3]:  
        if value[valSize-1] is None or float(value[valSize-1]) >= 0.9:
            # If confidence score is acceptiable, then check there are any non existant works that need to be reviewed
            in_dictionaries = wd.in_dictionaries(value[0])
            if in_dictionaries:
                value.append(0)
            else:
                value.append(1)
        else:  
            value.append(1)  
    return value  
  
# Function to convert flat dictionary with delimited keys into a nested dictionary
# This is a critical step in reformating CSV content to unflattened state so it can be converted to its original JSON form
def nested_dict(input_dict, delimiter='.'):  
    result_dict = {}  
    for key, value in input_dict.items():  
        parts = key.split(delimiter)  
        d = result_dict  
        for part in parts[:-1]:  
            if part not in d:  
                d[part] = {}  
            d = d[part]  
        d[parts[-1]] = value  
    return result_dict  
  
input_directory = 'csv/'  
output_directory = 'output/'  
os.makedirs(output_directory, exist_ok=True)  
  
# Find all CSV files in the input directory  
csv_files = glob.glob(os.path.join(input_directory, '*.csv'))  
  
for csv_file_path in csv_files:  
    df = pd.read_csv(csv_file_path) 

    # Apply procesing to data and convert to dictionary for convertion to JSON
    df = df.applymap(convert_to_list)  
    df = df.applymap(update_list)   
    flat_dict = df.to_dict(orient='records')[0]  
   
    nested_data = nested_dict(flat_dict)   
    formatted_json = json.dumps(nested_data, indent=4)  
  
    # Derive the output JSON file path from the input CSV file path  
    base_filename = os.path.splitext(os.path.basename(csv_file_path))[0]  
    output_json_path = os.path.join(output_directory, f'{base_filename}.json')  
  
    with open(output_json_path, 'w') as json_file:  
        json_file.write(formatted_json)  
  
print("CSV processing and convertion to JSON completed.")   