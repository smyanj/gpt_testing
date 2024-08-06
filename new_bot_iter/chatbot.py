from openai import OpenAI

client = OpenAI(api_key='')
import requests



# Get resources from the local API
def get_resources():
    response = requests.get("http://127.0.0.1:5000/api/resources")
    if response.status_code == 200:
        return response.json()
    return []

def chat_with_gpt(prompt):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content


def main():
    print("Welcome to the Python Learning Chatbot!")
    print("Ask me anything about learning Python.")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        
        gpt_response = chat_with_gpt(user_input)

        
        if "resource" in gpt_response.lower():
            resources = get_resources()
            if resources:
                # For simplicity, just take the first resource
                resource = resources[0]  
                resource_recommendation = (
                    f"Here is a recommended resource for you:\n"
                    f"Title: {resource['title']}\n"
                    f"Video: {resource['video']}\n"
                    f"Author: {resource['author']}\n"
                    f"Link: {resource['link']}\n"
                )
                print(resource_recommendation)
            else:
                print("Sorry, I couldn't find any resources at the moment.")
        else:
            print(f"GPT-3.5: {gpt_response}")

if __name__ == "__main__":
    main()