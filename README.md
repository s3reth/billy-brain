# Billy AI Server

Simple Flask server for Billy’s AI memory.

## Setup (GitHub)

1. Create a new repo named `billy-ai-server`
2. Copy in `app.py`, `requirements.txt`, `README.md`
3. Commit and push to GitHub

## Deploy to Render.com

1. In Render dashboard → New → Web Service
2. Select your repo
3. Fill these settings:
   - Environment: **Python**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
   - Leave root directory blank
4. Click **Create Web Service**
5. Wait ~2min for deployment; get your public URL

## Use from Roblox

```lua
local API_URL = "https://your-render-url"  -- from Render

local HttpService = game:GetService("HttpService")

-- Send movement:
HttpService:PostAsync(API_URL.."/movement", HttpService:JSONEncode({
    player = "PlayerName", 
    pos = {x=0,y=0,z=0}, 
    state = "Running", 
    timestamp = os.time()
}), Enum.HttpContentType.ApplicationJson)

-- Get latest:
local res = HttpService:GetAsync(API_URL.."/latest")
local data = HttpService:JSONDecode(res)
print(data.player, data.pos.x, data.state)
