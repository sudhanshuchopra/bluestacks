import os

# Third Party Imports
import discord
from dotenv import load_dotenv
from googleapiclient.discovery import build

# local imports
from models import History, session


# Loading .env variables into environment
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
API_KEY = os.getenv('API_KEY')
CSE_ID = os.getenv('CSE_ID')

MESSAGE_KEY = 'Hey'
MESSAGE_RESPONSE_KEY = 'Hi'
SEARCH_KEY = '!google'
HISTORY_KEY = '!recent'
MAX_ITEMS = 5

client = discord.Client()

@client.event
async def on_message(message):
    """
    Function to take actions on receiving messages
    :param message: message object from decord
    """
    RESPONSE = ''

    # return incase user is bot user only
    if message.author == client.user:
        return

    # handling simple Hey message
    if message.content == MESSAGE_KEY:
        RESPONSE = MESSAGE_RESPONSE_KEY

    # Search using google
    if message.content.startswith(SEARCH_KEY):
        service = build("customsearch", "v1", developerKey=API_KEY)
        search_term = message.content.split(SEARCH_KEY)[-1].strip()
        res = service.cse().list(q=search_term, cx=CSE_ID).execute()
        RESPONSE = ', '.join([item.get('link', '') for item in res['items'][:MAX_ITEMS]])
        history_obj = History(search_key=search_term)
        session.add(history_obj)
        session.commit()

    # History search
    if message.content.startswith(HISTORY_KEY):
        search_term = '%{}%'.format(message.content.split(HISTORY_KEY)[-1].strip())
        RESPONSE = ', '.join([
            history_obj[0] for history_obj in session.query(History.search_key).filter(
                History.search_key.like(search_term)
            ).all()
        ])

    # returning response
    await message.channel.send(RESPONSE)

client.run(TOKEN)
