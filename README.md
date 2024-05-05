# Telegram Sender

## Setup
- Get required information:
    - Create a bot:
        - Chat @BotFather in Telegram.
        - Type “/newbot” and follow the prompts to create a new bot.
    - Get chat id:
        - Chat @get_id_bot in Telegram.
- Create `.env` file
- Fill these parameters inside the `.env`:
    ```
    TOKEN="xxx"
    CHAT_ID="xxx"
    HTTP_PROXY="xxx"
    HTTPS_PROXY="xxx"
    PROXY_PORT="xxx"
    API_ID="xxx"
    API_HASH="xxx"
    ```
- Prepare the python environment:
    - Create environment `python -m venv .venv`
    - Activate the environment.
    - Install dependencies `pip install -r requirements.txt`