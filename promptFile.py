import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def return_answer(prompt):
  response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{
      "role": "system",
      "content": prompt
    }],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
  )

  return response.choices[0].message.content