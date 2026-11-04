# Pirate: MIT Module 3 practice bot

Adapted from the course starter project [avathuy/dbot](https://github.com/avathuy/dbot).
This version follows the updated course guide: OpenRouter supplies the AI model.

## What each part does

- Discord is the chat interface.
- Python listens for commands and sends replies.
- OpenRouter connects a question to an available free AI model.
- A private `.env` holds credentials and the permitted practice channel.
- The public `.env.example` contains only blank configuration fields.

## Setup

1. Install dependencies: `python -m pip install -r requirements.txt`.
2. Copy `.env.example` to `.env` and set `ALLOWED_CHANNEL_ID` to your practice channel.
3. Enter the Discord token safely: `python setup_keys.py TOKEN`.
4. Enter the OpenRouter key safely: `python setup_keys.py OPENROUTER_KEY`.

The hidden prompts do not display credentials or put them in shell history.
The local .env is ignored by Git. Never publish it or paste keys into chat.

## Test in two stages

Run `python discord_only.py`, then send `$hello` in the practice channel.
Stop that process with Ctrl+C before running `python mybot.py`.
Then try `$question What is the best treasure?`.
Only one bot process should run at a time.

The AI version uses `openrouter/free` with no paid fallback.
Free models can be slow, rate-limited, or temporarily unavailable.
Use fictional examples: questions are sent to OpenRouter and its model provider.
The bot only responds in the configured channel and ignores other bots.
It has no access to client systems and cannot schedule or approve actions.

## Ending a practice session

Stop the bot with Ctrl+C and stop the Codespace when you are finished.
This is a learning workspace, not continuous production hosting.

## Assignment status

Live Discord greeting, AI question, and empty-question help tests passed on November 4, 2026. A response-length issue was fixed and the marketing example passed on retest. See TEST_RESULTS.md.
The optional submission also needs a 100–300-word project explanation and a Discord link.
