# This function will check if each word contained in entry(string) is a word that matches an entry in wordlist.txt, if so return None, else return a list of false words
# Note each line in the text document is a word entry
# Words that consist of only numbers and special characters are not concidered
# False words are outputted in original casing
def get_fake_words(entry):
    dictionary = "dictionaries/wordlist.txt"
    with open(dictionary, 'r') as file:
        wordlist = file.read().splitlines()  
    
    fake_words = []
    words = entry.split()  
    for word in words:
        # TODO: check if word is only made up of ascii characters
        # Only check for words not only consisting of numbers and special characters
        if not all(c in '1234567890-/,() ' for c in word):
            # Comparisons are done not considering casing so lower case of word is evaluated
            if word.lower() not in wordlist:  
                fake_words.append(word)
    return fake_words

# This function will check if the word matches an entry in names.txt, if so return true, else return false
def check_name(word):
    dictionary = "dictionaries/firstNames.txt"
    with open(dictionary, 'r') as file:
        names = file.read().splitlines()
    return True if word in names else False

# This function will check if the word matches an entry in lastnames.txt, if so return true, else return false
def check_lastname(word):
    dictionary = "dictionaries/lastNames.txt"
    with open(dictionary, 'r') as file:
        lastnames = file.read().splitlines()
    return True if word in lastnames else False

# This function will check if the word matches an entry in abbreviations.txt, dfo-acronyms.txt, glosseries.txt, if so return true, else return false
# Note each line the text file is formatted like 'abbr.	 abbreviation' only the first part is the addreviation
def check_abbrev(word):
    dict_abbr = "dictionaries/abbreviations.txt"
    dict_acr = "dictionaries/dfo-acronyms.txt"
    dict_glos = "dictionaries/glosseries.txt"
    with open(dict_abbr, 'r') as file:
        # Split to take line content before whitespace since after whitespace is definition, and use strip to ignore lines of only whitespace
        abbreviations = [line.split()[0] for line in file if line.strip()]

    # If not in abbreviations, check dfo-acronyms
    if word in abbreviations:
        return True
    else:
        with open(dict_acr, 'r') as file:
            acronyms = [line.split()[0] for line in file if line.strip()]

        # If not in dfo-acronyms, check glosseries
        if word in acronyms:
            return True
        else:
            with open(dict_glos, 'r') as file:  
                glosseries = [line.split()[0] for line in file if line.strip()]

            # Return boolean if found in glosseries
            return True if word in glosseries else False

# Will add a given word to the wordlist dictionary if it exits
def add_word_to_wordlist(new_word):
    if get_fake_words(new_word):
        add_word_to_dictionary(new_word, "dictionaries/wordlist.txt")
    else:
        print(new_word+" already exists in the wordlist dictionary!")

# Will add the given word to a dictionary alphabetically
def add_word_to_dictionary(new_word, dictionary_path):  
    new_word = new_word.lower()
    # Read the current wordlist  
    with open(dictionary_path, 'r') as file:  
        words = file.read().splitlines()  
      
    # Insert the new word alphabetically  
    # Use a binary search algorithm for efficiency since the list is sorted  
    low, high = 0, len(words)  
    while low < high:  
        mid = (low + high) // 2  
        if words[mid] < new_word:  
            low = mid + 1  
        else:  
            high = mid  
      
    # 'low' is now the index where the new word should be inserted  
    words.insert(low, new_word)  
      
    # Write the updated wordlist back to the file  
    with open(dictionary_path, 'w') as file:  
        file.write('\n'.join(words)) 
    
    print(new_word+" has been added to the dictionary!")

# Takes in a string and returns True if each word exists in a dictionary and returns false otherwise
# None(null) values are treated as existant
def in_dictionaries(value):
    if value: # check if under acci is from 0 to 2
        # First check is normal english words, will ignore words of just numbers and special characters
        non_real_words = get_fake_words(value)
        if (non_real_words):
            # Second check is checking if each fake word is an abbrivation or acynom
            for fake_word in non_real_words:
                is_abbrev = check_abbrev(fake_word)
                if (not is_abbrev):
                    # Third/fourth check is checking if non word and non abbrivation is a name or last name
                    is_name = check_name(fake_word)
                    if (not is_name):
                        is_lastname = check_lastname(fake_word)
                        if (not is_lastname):
                            return False

    return True