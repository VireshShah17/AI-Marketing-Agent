BANNED_WORDS = [
    "hate",
    "violence",
    "kill",
    "racist",
    "terror"
]

def validate_caption(caption: str):
    caption_lower = caption.lower()
    for word in BANNED_WORDS:
        if word in caption_lower:
            return False, f"Unsafe word detected: {word}"

    if len(caption.strip()) < 20:
        return False, "Caption too short"

    return True, "Safe"
