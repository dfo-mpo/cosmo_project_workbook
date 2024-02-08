import json  
import os  
import glob  
import word_dictionary as wd

# Global configuration parameters
confidence_min = 0.9
source_path = 'input'
output_path = 'output'
  
# Function to recursively iterate through items in the JSON structure  
def iterate_items(item, indent=0):  
    if isinstance(item, dict):  
        for key, value in item.items():  
            print('  ' * indent + f"Key: {key}")  
            iterate_items(value, indent+1)  
    elif isinstance(item, list): 
        instance_flag = False
        for i, list_item in enumerate(item):  
            # Case when nested objects have no names themselves
            if isinstance(list_item, (dict, list)):  
                print('  ' * indent + f"List item {i}:")  
                iterate_items(list_item, indent+1)  
            # Case we looking through entries (input value and confidence) of a feild
            else:  
                print('  ' * indent + f"List item {i}: {list_item}")
                instance_flag = True
        
        if instance_flag: 
            review_required = 0

            # Value and confidence can be none so if conditions needed for those cases
            if item[1] and item[1] < confidence_min:
                print("Value: "+item[0]+" Confidence: "+'%.3f' % item[1])
                review_required = 1
            else:
                # Word check is ignored for empty of number values
                if item[0] and not all(c in '1234567890-/, ' for c in item[0]):
                    fake_words = wd.get_fake_words(item[0])
                    if fake_words:
                        for fake_word in fake_words:
                            is_abbrev = wd.check_addrev(fake_word)
                            if not is_abbrev:
                                confidence_str = '%.3f' % item[1] if item[1] else 'none'
                                print("Value: "+item[0]+" Confidence: "+ confidence_str)
                                review_required = 1
                                break
            item.append(review_required)

    else:  
        print('  ' * indent + f"Value: {item}")  
    
 
json_files = glob.glob(os.path.join(source_path, '*.json'))  
  
# Iterate through each JSON file in the directory  
for json_file_path in json_files:  
    print(f"Processing file: {json_file_path}") 
    file_name = json_file_path.split('\\')[1] 
    with open(json_file_path, 'r') as json_file:  
        try:  
            data = json.load(json_file)  
            iterate_items(data)

            with open(output_path+'/'+file_name, 'w') as json_file:
                json.dump(data, json_file, indent=4)

            print("\n")  
        except json.JSONDecodeError as e:  
            print(f"Error reading JSON file {json_file_path}: {e}")  
  
    print("Finished processing file.\n")  