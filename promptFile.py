import os
import openai
from dotenv import load_dotenv
load_dotenv()
import requests
import io
from PIL import Image
import json

hf_key = os.getenv("HG_FACE")
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {hf_key}"}

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

def return2 (prompt):
  response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{
      "role": "system",
      "content": f'Give a description about the topic {prompt} in english and spanish. Also generate a suitable prompt about the given prompt to put into a stable diffusion model to generate image. Return in a dictionary type of 3 keys(eng, spa, image)'
    }],
  temperature=1,
  max_tokens=1000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
  )
  resp = (response.choices[0].message.content)
  
  data = json.loads(resp)
  eng_part = data["eng"]
  spa_part = data["spa"]
  img = data["image"]
  print(img)
  
  response = requests.post(API_URL, headers=headers, json={'inputs' : f'{img}'}).content
  image = Image.open(io.BytesIO(response))
  file_path = f"./images/{img}.jpg"  

  image.save(file_path)

  return resp

if __name__ == '__main__':
  print(return2('who is shah rukh khan'))


# import requests

# API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
# headers = {"Authorization": "Bearer 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"}

# def query(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.content
# image_bytes = query({
# 	"inputs": "Astronaut riding a horse",
# })
# # You can access the image with PIL.Image for example
# import io
# from PIL import Image
# image = Image.open(io.BytesIO(image_bytes))
