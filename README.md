# ✉️ Email Polisher

An AI-powered web application that converts rough, informal messages into clear and professional emails instantly.

Enter a raw message (e.g., "fix this bug now"), and the app rewrites it into a structured business email with subject, greeting, and closing.

---

## ✨ Features

🔍 Enter rough email text  
🎯 Select tone (Professional, Friendly, Formal, etc.)  
🪄 Automatically adds subject, greeting & closing  
📋 One-click copy polished email  
⚡ Fast local AI processing using Ollama  
💻 Runs without paid APIs  
🔒 Privacy-friendly (local inference)

---

## 🛠 Tech Stack

Next.js (App Router)  
TypeScript  
Tailwind CSS  
Ollama (Local LLM Engine)  
gemma:2b model (Lightweight AI Model)

---

## 📂 Project Structure


### Folder Responsibilities

app/api/polish/ → Backend API route  
app/page.tsx → Main UI page  
styles/ → Tailwind styling  
public/ → Static assets  

---

## 🧠 How It Works

1. User enters a rough message.
2. User selects a tone.
3. API route sends prompt to Ollama.
4. Local AI model (gemma:2b) rewrites the email.
5. The polished email is displayed in the output section.

All AI processing happens locally via Ollama.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/reetikachoudhary15-hue/Email-Polishers.git
cd email-polisher
```

2️⃣ Install Dependencies
npm install

3️⃣ Install Ollama

Download from:

https://ollama.com

Verify installation:

ollama --version

4️⃣ Download AI Model
ollama pull gemma:2b

5️⃣ Run Development Server
npm run dev

6️⃣ Open in Browser
http://localhost:3000

📊 Example Usage

Input:

i want one day leave


Output:

Subject line added

Proper greeting

Professional tone

Clear closing


🔮 Future Improvements

AI-based email reply generator
Gmail integration
Chrome extension
Cloud deployment version
Multi-language support

🎯 Project Goals

This project demonstrates:

Full-stack development with Next.js
AI integration using local LLM
Cost-efficient AI architecture
Prompt engineering basics
Performance optimization for low-resource systems

🧪 Testing

You can test different inputs and tone options directly in the UI.

Example test inputs:

send me the report fast

fix this issue urgently

🧑‍💻 Author

Reetika Choudhary
BCA(DATA SCIENCE) Student  



---




