# This function will check if each word contained in entry(string) is a word that matches an entry in wordlist.txt, if so return None, else return a list of false words
# Note each line in the text document is a word entry
# False words are outputted in lowercase
def get_fake_words(entry):
    dictionary = "dictionaries/wordlist.txt"
    with open(dictionary, 'r') as file:
        wordlist = file.read().splitlines()  
    
    fake_words = []
    words = entry.lower().split()  
    for word in words:  
        if word not in wordlist:  
            fake_words.append(word)
    return fake_words

# This function will check if the word matches an entry in names.txt, if so return true, else return false
# assumes word is lower case
def check_name(word):
    dictionary = "dictionaries/names.txt"
    with open(dictionary, 'r') as file:
        names = file.read().splitlines()
    return True if word in names else False

# This function will check if the word matches an entry in en-abbreviations.txt, if so return true, else return false
# Note each line the text file is formatted like 'abbr.	 abbreviation' only the first part is the addreviation
# assumes word is lower case
def check_addrev(word):
    dictionary = "dictionaries/en-abbreviations.txt"
    with open(dictionary, 'r') as file:  
        abbreviations = [line.split('\t')[0] for line in file.readlines()]  
    return True if word in abbreviations else False  

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