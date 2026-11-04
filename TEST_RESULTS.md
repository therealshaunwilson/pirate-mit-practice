# Pirate practice bot: test results

Date: November 4, 2026

## Live Discord tests
- Basic bot: $hello returned Hello!.
- AI bot: $question What is the best treasure? returned a complete pirate-style answer.
- Empty $question returned command help without making an AI request.
- A request for three marketing ideas for a fictional neighborhood bakery initially ended mid-answer. OpenRouter reported finish_reason=length at the original 500-token limit.
- Increased the response limit to 1,500 tokens and added an explicit notice when a response is incomplete.
- Retested the same bakery question: all three ideas were returned, with finish_reason=stop. The routed model was nvidia/nemotron-3-ultra-550b-a55b:free.

## Configuration and checks
- AI requests use openrouter/free with no paid fallback.
- The bot responds only in the configured practice channel and ignores other bots.
- Offline checks covered wrong-channel messages, bot messages, ordinary chat, empty questions, and missing AI credentials.
- Python syntax checks passed.
- The private .env is excluded from Git, is not tracked, and has owner-only permissions. Real credentials were not published.

## What this demonstrates
Discord provides the interface, Python handles commands, and OpenRouter supplies a model response. This is a learning prototype, not an MCP integration with client systems. It cannot access client data, schedule work, or take external actions. Generated suggestions still require human review.

The bot stays online only while its Python process and Codespace are running. Free-model availability and response speed can vary.

## Coursework remaining
The optional submission still needs a 100-300-word project explanation and a Discord link. The separate required email-style proposal also remains to be completed.
