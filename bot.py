import os
import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API = f"https://api.telegram.org/bot{TOKEN}/"

def send_message(chat_id, text):
    requests.post(API + "sendMessage", json={
        "chat_id": chat_id,
        "text": text
    })

def main():
    offset = 0
    while True:
        data = requests.get(
            API + "getUpdates",
            params={"offset": offset, "timeout": 30},
            timeout=35
        ).json()

        for update in data.get("result", []):
            offset = update["update_id"] + 1
            msg = update.get("message", {})
            chat_id = msg.get("chat", {}).get("id")
            text = msg.get("text", "")

            if chat_id and text == "/start":
                send_message(
                    chat_id,
                    "Welcome! 📊 Apon AI Signal Bot\n"
                    "Send /analysis for market analysis help.\n"
                    "This bot does not execute trades."
                )
            elif chat_id and text == "/analysis":
                send_message(
                    chat_id,
                    "📊 Market Analysis\n"
                    "No live market data connected yet.\n"
                    "Send a chart screenshot to ChatGPT for analysis."
                )

if __name__ == "__main__":
    main()
