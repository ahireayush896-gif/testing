⚠️ **AUTO Multi-Engine Dispatcher: All candidate models exhausted**

The AI Dispatcher attempted to route your task across specialized engines, but each provider encountered quota or balance limits:

- **gemini-3.8-flash**: Google Gemini API quota reached (HTTP 429). Free tier per-minute or daily quota exhausted. Free quota refreshes in 80543 seconds. Please retry shortly or upgrade at https://aistudio.google.com.
- **claude-3-5-sonnet-20241022**: Active rate-limit cooldown (23s remaining)
- **gpt-4o**: OpenAI GPT-4o quota exhausted (HTTP 429): You have no credits remaining. Add credits to continue using the API at https://platform.openai.com/settings/organization/billing/. Please check billing and add credits at https://platform.openai.com/account/billing or select another model.
- **gemini-3.5-flash**: Google Gemini API quota reached (HTTP 429). Free tier per-minute or daily quota exhausted. Free quota refreshes in 80542 seconds. Please retry shortly or upgrade at https://aistudio.google.com.
- **deepseek-reasoner**: DeepSeek Reasoner balance exhausted (HTTP 402): Insufficient Balance (request_id: c4cad737-9c95-49c9-a002-15e7b8b6e108) Please recharge your account balance at https://platform.deepseek.com or select another model.

👉 **Resolution**: Please top up credits for any of the above providers in your `.env` or wait for rate limit cooldowns to refresh.