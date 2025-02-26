# 🦙 Ollama + DeepSeek + Open WebUI Chatbot 🗨️  

🚀 This guide helps you **set up and run a local AI chatbot** using **Ollama, DeepSeek LLM, and Open WebUI**.  

1️⃣ Ollama Setup Locally** 🛠️  
✅ **Download Ollama** 👉 [Get it here](https://ollama.com/)  
✅ **Start Ollama Locally**   
ollama serve

2️⃣ Download & Run DeepSeek LLM 🤖

✅ Run DeepSeek with default setup (7B model)
ollama run deepseek-r1  # Runs DeepSeek-R1 (7B Model)

✅ Download & Use a Specific DeepSeek Model
ollama pull deepseek-r1:1.5b  # Pulls smaller DeepSeek model (1.5B)

✅ Test DeepSeek Model
ollama run deepseek-r1:1.5b "What is DeepSeek AI?"


3️⃣ Open WebUI Setup 🌐

📌 Option 1: Install Open WebUI via pip
pip install open-webui
open-webui serve

📌 Option 2: Run Open WebUI using Docker 🐳
docker run -d -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --name open-webui --restart always \
  ghcr.io/open-webui/open-webui:main