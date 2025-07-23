import pandas as pd

def read_budget(csv_path):
    """
    Reads a budget file and returns a DataFrame.

    Args:
        file_path (str): The path to the budget file.

    Returns:
        pd.DataFrame: A DataFrame containing the budget data.
    """
    try:
        df = pd.read_csv(csv_path)
        # Check if the required columns are present
        if not {'Type', 'Name', 'Montant'}.issubset(df.columns):
            raise Exception('The budget file is not in the correct format. It must contain Type, Name, and Montant columns.')

        # Filtrage des lignes
        revenues = df[df['Type'].str.lower() == 'revenu']
        depense = df[df['Type'].str.lower() == 'dépense']
        return revenues, depense

    except FileNotFoundError:
        raise FileNotFoundError(f"The file {csv_path} does not exist.")
    except pd.errors.EmptyDataError:
        raise ValueError("The file is empty.")
    except pd.errors.ParserError:
        raise ValueError("The file could not be parsed. Please check the file format.")


def calculating_budget(revenues, depense):
    """
    Calculates the total budget from revenues and spending DataFrames.

    Args:
        revenues (pd.DataFrame): DataFrame containing revenue data.
        depense (pd.DataFrame): DataFrame containing spending data.

    Returns:
        dict: A dictionary containing the total revenue, total spending, remaining budget, savings rate, and spending rate.
    """
    # Nettoyer et convertir les colonnes 'Montant' en nombres
    revenues['Montant'] = pd.to_numeric(revenues['Montant'].str.replace('€', ''), errors='coerce')
    depense['Montant'] = pd.to_numeric(depense['Montant'].str.replace('€', ''), errors='coerce')

    total_revenue = revenues['Montant'].sum()
    total_depense = depense['Montant'].sum()
    reste_budget = total_revenue - total_depense
    taux_epargne = round(reste_budget / total_revenue, 2) if total_revenue > 0 else 0
    taux_depense = round(total_depense / total_revenue, 2) if total_revenue > 0 else 0

    return {
        'total_revenue': total_revenue,
        'total_depense': total_depense,
        'reste_budget': reste_budget,
        'taux_epargne': taux_epargne,
        'taux_depense': taux_depense
    }