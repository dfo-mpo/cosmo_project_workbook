import openai
import pandas as pd

# Set your OpenAI API key
openai.api_type = "azure"
openai.api_base = "https://pssiopenai-163oxygen.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = "9c99b1e94cbc489dbff13f12b69798f7"
model_id = "gpt-4-turbo-1106p"

def read_csv_using_gpt(prompt, csv_content):
    # Combine the prompt and CSV content
    conversation = [{'role': "system", "content": f"You are an AI assistant that reads in a CSV and answers user questions only using information from it.\nCSV:\n{csv_content}"}]
    conversation.append({'role': 'user', 'content': prompt})
    response = openai.ChatCompletion.create(
        engine=model_id,
        messages=conversation,
        temperature=0.3,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)

    return response.choices[0].message.content

print("opening document")
csv_file_path = "sample1.csv"  # Replace with the path to your CSV file
df = pd.read_csv(csv_file_path)
csv_content = df.to_csv(index=False)

# # Example prompt
# prompt = "Generate a summary of the CSV data."
# # Get the GPT-3.5 Turbo response
# result = read_csv_using_gpt(prompt, csv_content)
# # Display the result
# print(result)
# List all values that have less than 0.8 confidence or not complete words

while True:
    user_input = input("Enter something (or type 'exit' to quit): ")

    # Process the user input
    if user_input.lower() == 'exit':
        break
    else:
        print("Question for GPT4 Turbo:", user_input)
        print(read_csv_using_gpt(user_input, csv_content))



