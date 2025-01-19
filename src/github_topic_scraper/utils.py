import os
from typing import Dict, Union

def parse_star_count(stars_text: str) -> int:
    stars_text = stars_text.strip()
    if stars_text[-1] == 'k':
        return int(float(stars_text[:-1]) * 1000)
    return int(stars_text)

def ensure_output_directory(directory: str) -> None:
    os.makedirs(directory, exist_ok=True)

def sanitize_filename(filename: str) -> str:
    return filename.lower().replace(' ', '_')