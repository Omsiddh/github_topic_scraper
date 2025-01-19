import os
from typing import Dict, Union

def parse_star_count(stars_text: str) -> int:
    """
    Parse GitHub star count from text format.
    
    Args:
        stars_text (str): Star count text (e.g., "1.2k" or "500")
        
    Returns:
        int: Numeric star count
    """
    stars_text = stars_text.strip()
    if stars_text[-1] == 'k':
        return int(float(stars_text[:-1]) * 1000)
    return int(stars_text)

def ensure_output_directory(directory: str) -> None:
    """
    Create output directory if it doesn't exist.
    
    Args:
        directory (str): Directory path
    """
    os.makedirs(directory, exist_ok=True)

def sanitize_filename(filename: str) -> str:
    """
    Convert a string to a valid filename.
    
    Args:
        filename (str): Input string
        
    Returns:
        str: Valid filename
    """
    return filename.lower().replace(' ', '_')
