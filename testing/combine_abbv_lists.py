# This script can be used to alhabetically combine text file lists for acrynoms and/or abbriviations together

def parse_entry(line):  
    # Splits each entry into abbreviation and meaning  
    parts = line.strip().split("\t")  
    return parts[0], " ".join(parts[1:])  
  
# Read entries from the existing file  
existing_entries = []  
with open('dictionaries/abbreviations.txt', 'r') as file:  
    existing_entries = [parse_entry(line) for line in file if line.strip()]  
  
# Read entries from the new entries file  
new_entries = []  
with open('test.txt', 'r') as file:  
    new_entries = [parse_entry(line) for line in file if line.strip()]  
  
# Combine the lists  
all_entries = existing_entries + new_entries  
  
# Sort the combined list alphabetically by abbreviation  
all_entries.sort(key=lambda x: x[0])  
  
# Write the sorted entries back to a file or print them  
with open('sorted_entries.txt', 'w') as file:  
    for abbreviation, meaning in all_entries:  
        file.write(f"{abbreviation}\t{meaning}\n")  