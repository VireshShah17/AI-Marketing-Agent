import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_caption(brand, strategy = None):
    strategy_text = strategy if strategy else "Follow standard brand tone."
    prompt = f"""
        You are a professional LinkedIn marketing content creator.

        Brand Name: {brand.name}
        Tone: {brand.tone}
        Target Audience: {brand.target_audience}

        Strategy Adjustment:{strategy_text}

        Write:
        - A short engaging LinkedIn caption
        - Include 3 relevant hashtags
        - Add a strong CTA
    """
    response = requests.post(OLLAMA_URL, json = {"model": "phi", "prompt": prompt, "stream": False})

    return response.json()["response"]