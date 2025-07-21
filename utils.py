from datetime import datetime
import os

def format_monnaie(euros):
    """
    Format a number as a currency string with two decimal places.
    """
    return f"{euros,: .2f}€".replace(',', '')

def get_month_label():
    """
    Get the current month label in the format.
    """
    return datetime.now().strftime("%Y-%m-%d")

def generate_filename(prefix, ext='png'):
    """
    Generate a filename.
    """

    return f"{prefix}.{get_month_label()}.{ext}"

def ensure_directory_exists(path):
    """
    Ensure that the directory exists, creating it if necessary.
    """
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def recommendation_message():
    """
    Return a recommendation message.
    """
    