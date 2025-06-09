# locations_a2a

This repo retrieves Kroger store locations using Google Agent2Agent ADK with Kroger Store Location Public API as a mcp tool. 

You can set up your local delopment:

cd ~/

git clone https://github.com/google-a2a/a2a-samples.git

git clone https://, put kroger_agent under directory ~/a2a-samples/samples/a2a-adk-app/

cd kroger_agent

vim .env with KROGER_API_KEY, KROGER_CLIENT_ID, KROGER_CLIENT_SECRET, KROGER_REDIRECT_URI, KROGER_USER_ZIP_CODE

1. set up remote agent
   
cd ~/a2a-samples/samples/a2a-adk-app/

source .venv/bin/activate

cd kroger_agent

uv run .

http:/localhost:10001

2. set up adk demo ui

cd ~/a2a-samples/demo/ui

uv run main.py

http://localhost:12000

add remote agent: localhost:10001 save

3. ask questions to list top 5 Kroger stores within 10 miles radius for any zipcode, such as 98001. 

References:

Google a2a: https://github.com/google-a2a/a2a-samples.git

kroger-api: https://github.com/CupOfOwls/kroger-api
