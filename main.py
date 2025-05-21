from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import openai
import base64
import os

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/analyze")
async def analyze_trade(image: UploadFile = File(...), news: str = Form(...)):
    try:
        image_bytes = await image.read()
        img_base64 = base64.b64encode(image_bytes).decode()

        response = openai.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {"role": "system", "content": "You are a forex trading analyst. Provide a clear trade suggestion based on chart and news."},
                {"role": "user", "content": [
                    {"type": "text", "text": f"Here is a forex chart and related news: {news}"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_base64}"}}
                ]}
            ],
            max_tokens=800
        )

        trade_idea = response.choices[0].message.content
        return {"result": trade_idea}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
