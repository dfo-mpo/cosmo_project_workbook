# The perpose of this script is to covert the jsons in the input folder to creat CSVs in the csv folder that are flattened.
# These flattened CSVs are easy to work with for analysis and adding additional information
import json  
import os  
import pandas as pd  
  
source_directory = 'input/'  
output_directory = 'csv/'   

# Function that uses pandas to flatten and convert a json to csv
def pandas_flatten(json_file, csv_file):  
    with open(json_file, 'r') as file:  
        data = json.load(file)  
     
    flattened_data = pd.json_normalize(data)  
    flattened_data.to_csv(csv_file, index=False)  
    print(f"CSV file created at: {csv_file}")  
  
# Make sure the output directory exists  
if not os.path.exists(output_directory):  
    os.makedirs(output_directory)  
  
# Iterate over each file in the source directory  
for filename in os.listdir(source_directory):  
    if filename.endswith('.json'):  
        # Create path for csv output of same name
        json_path = os.path.join(source_directory, filename)   
        csv_filename = filename.replace('.json', '.csv')  
        csv_path = os.path.join(output_directory, csv_filename)  

        pandas_flatten(json_path, csv_path)  


# OLD LEGACY CODE FOR NOT USING PANDAS
# Function to flatten the JSON data.
# def flatten_json(y):
#     out = OrderedDict()

#     def flatten(x, name=''):
#         if isinstance(x, dict):
#             for a in x:
#                 flatten(x[a], f"{name}{a}_")
#         elif isinstance(x, list):
#             i = 0
#             for a in x:
#                 flatten(a, f"{name}{i}_")
#                 i += 1
#         else:
#             out[name[:-1]] = x

#     flatten(y)
#     return out

# def manual_flatten():
#     # Load the JSON data from a file.
#     with open(source, 'r') as json_file:
#         json_data = json.load(json_file)

#     # Flatten the JSON data.
#     flattened_data = flatten_json(json_data)

#     # Write the flattened data to a CSV file.
#     with open(output, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(flattened_data.keys())  # Write headers to CSV
#         writer.writerow(flattened_data.values())  # Write values to CSV

#     print("CSV file created successfully!")