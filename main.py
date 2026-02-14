from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class EmailRequest(BaseModel):
    text: str
    tone: str

@app.post("/polish")
async def polish_email(req: EmailRequest):

    prompt = f"""
    Rewrite the following message into a polite and professional email.

    Tone: {req.tone}

    Include:
    - Subject line
    - Greeting
    - Clear body
    - Professional closing

    Message:
    {req.text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return {"output": response.choices[0].message.content}
