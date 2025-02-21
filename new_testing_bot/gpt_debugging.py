from openai import OpenAI

client = OpenAI(api_key='')

try:
    response = client.completions.create(engine="text-davinci-003",
    prompt="Tell me a joke",
    max_tokens=150)
    print(response.choices[0].text.strip())
except Exception as e:
    print(f"Error: {e}")
