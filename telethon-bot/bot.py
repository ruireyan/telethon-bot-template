""" IMPORTS """
from telethon import TelegramClient, events


""" VARS """
api_id = API_ID
api_hash = 'API_HASH'
bot_token = 'BOT_TOKEN'

client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)


""" START """
@client.on(events.NewMessage(pattern='/start'))
async def start(event): 
    chat_id = event.chat_id
    await client.send_message(chat_id, 'reyan is smart and cool :)))') #add your start message

    
""" RUN CLIENT """
client.run_until_disconnected()
