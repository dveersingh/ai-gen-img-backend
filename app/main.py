import httpx
import os
from fastapi import FastAPI, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import base64

load_dotenv()

app = FastAPI()

# Enable CORS for all origins (adjust in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HF_TOKEN = os.getenv("HF_TOKEN")

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Image Generator API (Hugging Face Version)"}

@app.post("/generate-image")
async def generate_image(prompt: str = Form(...)):
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {"inputs": prompt}

    timeout = httpx.Timeout(120.0, connect=20.0)

    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.post(
                "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2",
                headers=headers,
                json=payload
            )
            response.raise_for_status()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))

    image_data = response.content
    img_base64 = base64.b64encode(image_data).decode("utf-8")

    return {"message": "Image generated", "image_base64": img_base64}
