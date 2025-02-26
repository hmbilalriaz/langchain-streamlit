#Ollama SetUp Locally
Downloaded Ollama from https://ollama.com/
Start Ollama locally

#Deepseek download and run
ollama run deepseek-r1       #for default setup i-e 7b

#Open WebUi Setup via https://github.com/open-webui/open-webui
pip install open-webui
open-webui serve
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
