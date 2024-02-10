#import MerWebPy as mwp
import csv
import openai

# Set your OpenAI API key
openai.api_type = "azure"
openai.api_base = "https://pssiopenai-163oxygen.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = "9c99b1e94cbc489dbff13f12b69798f7"
model_id = "gpt-4-turbo-1106p"

csv_file_path = "output.csv"  # Replace with the path to your CSV file

# Uses GPT to check if a given work is real. GPT is instructed to behave like a function, returning only True or False
def gpt_check_word(entry):
    # Combine the prompt and CSV content
    conversation = [{'role': "system", "content": """You are a function that takes in an entry and returns True or False. 
                     Check if each word in the given entry is a real word in the English language or a name. If true then return True.
                     Note, unselected is a real word
                     If any word detected to not be a real word or name is checked if it is an acynom or abbrivation. If true then return True.
                     Else return false."""}]
    conversation.append({'role': 'user', 'content': entry})
    response = openai.ChatCompletion.create(
        engine=model_id,
        messages=conversation,
        temperature=0.3,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)

    return response.choices[0].message.content

# Open and read the CSV file
with open(csv_file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    transposed_data = zip(*csv_reader)
    confidenceVal = False
    lastVal = ''
    output = []

    for column in transposed_data:
        if not confidenceVal:
            lastVal = column[1]
        elif column[1] != '':
            confidence = float(column[1])
            if confidence < 0.8:
                output.append("Value: "+lastVal+" Confidence: "+column[1])
        # elif:
            is_real = gpt_check_word(lastVal)
            if (is_real == "False"):
                output.append("Value: "+lastVal+" Confidence: "+column[1])
        
        confidenceVal = not confidenceVal
    
    for i in output:
        print(i)


