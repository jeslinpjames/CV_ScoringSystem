def clean_text(text):
    """Remove extra whitespace and special characters."""
    return re.sub(r"\s+", " ", text).strip()
