"""First test: a fixed greeting, with no AI request."""
import os
import discord
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents, allowed_mentions=discord.AllowedMentions.none())
channel_id = int(os.getenv("ALLOWED_CHANNEL_ID") or "0")

@client.event
async def on_ready():
    print(f"Connected as {client.user}. Ready for $hello.", flush=True)

@client.event
async def on_message(message):
    if message.author.bot or message.channel.id != channel_id:
        return
    if message.content.strip() == "$hello":
        await message.channel.send("Hello!")

if __name__ == "__main__":
    token = os.getenv("TOKEN")
    if not token or not channel_id:
        raise SystemExit("Set TOKEN and ALLOWED_CHANNEL_ID in your private .env first.")
    client.run(token)
