from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True

multicast_bot = commands.Bot(command_prefix='?', intents=intents)

input_channel = 1127278101966098545
output_channels = [
    836412577167835136, # herolfg playground:test
    830447454813683723, # herolfg:gavin
]

@multicast_bot.event
async def on_message(message):
    if message.channel.id == input_channel:
        for channel_id in output_channels:
            channel = multicast_bot.get_channel(channel_id)
            await channel.send(message.content)

multicast_bot.run(DISCORD_TOKEN)

