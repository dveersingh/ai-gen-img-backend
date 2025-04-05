# AI Image Generator Backend (FastAPI + Hugging Face)

This is the backend for the AI Image Generator app, built with **FastAPI**. It connects with Hugging Face's **Stable Diffusion** model to generate images from text prompts and returns the image in base64 format.

## 🚀 Features
- FastAPI backend with async Hugging Face API calls
- Hugging Face token-based authentication
- Image returned as base64 for easy frontend rendering
- CORS enabled for frontend integration

---

## 📁 Project Structure
```
ai-generate-image/
  backend/
    app/
      main.py
    .env
    requirements.txt
    .gitignore
```

---

## 🧪 Local Development

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup `.env`
Create a `.env` file in the backend directory with:
```env
HF_TOKEN=your_huggingface_api_token_here
```

### 3. Run the server
```bash
uvicorn app.main:app --reload
```
The API will be available at `http://localhost:8000`

---

## 🧾 API Endpoints

### `POST /generate-image`
Generates an image based on a given text prompt.

**Form Data:**
- `prompt`: (string) text description

**Response:**
```json
{
  "message": "Image generated",
  "image_base64": "<base64-encoded-image>"
}
```

---

## 🚀 Deployment
This backend can be deployed to **Render**, **AWS**, or any cloud service.
Make sure to:
- Set the `HF_TOKEN` as an environment variable in the platform
- Set build/start commands appropriately (e.g., `uvicorn app.main:app`)

---

## 📜 License
MIT License

