import requests
import os
from dotenv import load_dotenv
load_dotenv()
import io
from PIL import Image

HG_FACE = os.getenv("HG_FACE")

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {HG_FACE}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content



if __name__ == "__main__":
    image_bytes = query({
	"inputs": "Astronaut riding a horse",
    })
    image = Image.open(io.BytesIO(image_bytes))