
from openai import OpenAI



client = OpenAI(api_key = "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")


def chat_gpt_query(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"content": prompt,"role": "user"}],
        max_tokens=(1000) ,  # Adjust this value based on the desired response length
        n=1,
        temperature=0.5,
    )
    return response.choices[0].message.content


### CHATGPT Stuff ###
# Set up the OpenAI API client (API key needed)
responses = []
prompts = []
prompt = "Write in-depth notes on the following artwork: \n" # !!!!! change prompt as needed


# Read the file and send lines to the ChatGPT API
with open("art.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line != "":
            fullPrompt = prompt + line
            response = chat_gpt_query(fullPrompt)
            if response != None:
                responses.append(response)
                prompts.append(line)
            else:
                print(f"Input did not execute: {line}\n ")


# Write the responses and their prompts to an output file
with open("output_file.txt", "a") as output_file:
    for i in range(len(responses)):
        output_file.write(f"Input: {prompts[i]}\n\n")
        output_file.write(f"Response: {responses[i]}\n")
        output_file.write("\n" + "=" * 50 + "\n\n")
