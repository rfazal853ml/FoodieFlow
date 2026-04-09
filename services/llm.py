import httpx
import json
import config


async def generate(prompt: str) -> dict:
    """Send prompt to Ollama and return parsed JSON response."""
    payload = {
        "model": config.OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "format": "json",
    }
    print("LLM Working...")

    async with httpx.AsyncClient(timeout=300) as client:
        response = await client.post(
            f"{config.OLLAMA_BASE_URL}/api/generate",
            json=payload,
        )
        response.raise_for_status()

    raw = response.json().get("response", "")
    print(raw)

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # Strip markdown fences if model wraps output
        cleaned = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        return json.loads(cleaned)