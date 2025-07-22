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

def recommendation_message(taux_depense, taux_epargne):

    """
    Return a recommendation message based on spending and saving rates.
    """
    if taux_depense > 0.8:
        return "You are spending too much. Consider reducing your expenses."
    elif taux_epargne < 0.1:
        return "You're not saving enough. Try to save at least 10% of your income."
    elif taux_depense < 0.5 and taux_epargne > 0.2:
        return "Your budget is balanced. Keep up the good work!"
    else:
        return "Your spending and saving rates are moderate. Keep an eye on your budget to ensure financial stability."
