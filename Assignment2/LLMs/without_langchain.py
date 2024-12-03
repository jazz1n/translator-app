import requests

METIS_API_KEY = "tpsg-93mG9D2eAH6FXqsH6BAPOVAFNfK67H1"
BOT_ID = "3ccade0d-b6c4-4bf8-8130-94a7bc41f94b"

# Function to create a conversation session
def create_conversation(bot_id: str, initial_message: str, api_key: str):
    url = "https://api.metisai.ir/api/v1/chat/session"
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "botId": bot_id,
        "user": None,
        "initialMessages": [
            {
                "type": "USER",
                "content": initial_message
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Function to send a message to the conversation session
def send_message(session_id: str, message: str, api_key: str):
    url = f"https://api.metisai.ir/api/v1/chat/session/{session_id}/message"
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "message": {
            "content": message,
            "type": "USER"
        }
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Chain class for managing interaction with Metis API
class MetisChain:
    def __init__(self, bot_id: str, api_key: str):
        self.bot_id = bot_id
        self.api_key = api_key
        self.session_data = create_conversation(bot_id, "Let's start the translation session.", api_key)
        self.session_id = self.session_data['id']

    def invoke(self, message: str):
        # Prepend translation instruction to the message
        instruction = "Translate the following sentence from English to Persian: "
        response_data = send_message(self.session_id, instruction + message, self.api_key)
        bot_response = response_data['content']
        return bot_response

# Initialize MetisChain
metis_chain = MetisChain(BOT_ID, METIS_API_KEY)

# Example message to translate
message_to_translate = "I love programming."

# Invoke translation
translated_result = metis_chain.invoke(message_to_translate)

# Output the result
print(f"Translated Result: {translated_result}")
