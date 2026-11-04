"""MIT practice bot: Discord commands connected to OpenRouter."""
import asyncio
import os
import discord
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
channel_id = int(os.getenv("ALLOWED_CHANNEL_ID") or "0")
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents, allowed_mentions=discord.AllowedMentions.none())
model = "openrouter/free"
ai_lock = asyncio.Lock()

def ask_pirate(question):
    # The OpenAI library connects to OpenRouter, as the course guide specifies.
    with OpenAI(
        api_key=os.environ["OPENROUTER_KEY"],
        base_url="https://openrouter.ai/api/v1",
        timeout=45.0,
        max_retries=0,
    ) as router:
        result = router.chat.completions.create(
            model=model,
            max_tokens=500,
            messages=[
                {"role": "system", "content": (
                    "You are Pirate, a friendly practice bot for an AI course. "
                    "Answer in a light pirate voice. Be useful and concise, "
                    "usually under 120 words. Admit uncertainty. You cannot "
                    "access private systems, schedule tasks, or take external actions."
                )},
                {"role": "user", "content": question},
            ],
        )
        return (result.choices[0].message.content or "").strip()

@client.event
async def on_ready():
    print(f"Connected as {client.user}. Commands: $hello and $question.", flush=True)

@client.event
async def on_message(message):
    if message.author.bot or message.channel.id != channel_id:
        return
    content = message.content.strip()
    command, _, question = content.partition(" ")
    if command == "$hello":
        await message.channel.send("Ahoy! Ask me with $question followed by your question.")
        return
    if command != "$question":
        return
    question = question.strip()
    if not question:
        await message.channel.send("Try: $question What is the best treasure?")
        return
    if not os.getenv("OPENROUTER_KEY"):
        await message.channel.send("My AI connection still needs its OpenRouter key.")
        return
    if ai_lock.locked():
        await message.channel.send("One moment, matey. Please try again after my current reply.")
        return
    async with ai_lock:
        try:
            # A worker thread keeps Discord responsive while the model answers.
            async with message.channel.typing():
                reply = await asyncio.to_thread(ask_pirate, question)
        except Exception as error:
            print(f"AI request failed: {type(error).__name__}", flush=True)
            await message.channel.send(
                "Arrr, the AI service could not answer just now. Please try again later."
            )
            return
        if not reply:
            await message.channel.send("Arrr, I got an empty answer. Please try again.")
            return
        # Discord messages must be shorter than 2,000 characters.
        for start in range(0, len(reply), 1900):
            await message.channel.send(reply[start:start + 1900])

if __name__ == "__main__":
    token = os.getenv("TOKEN")
    if not token or not channel_id:
        raise SystemExit("Set TOKEN and ALLOWED_CHANNEL_ID in your private .env first.")
    client.run(token)
