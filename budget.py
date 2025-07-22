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
        if not {'Type', 'Name','Montant' }.issubset(df.columns):
            raise Exception('The budget file is not in the correct format. It must contain Type, Name, and Amount columns.')
        
    except FileNotFoundError:
        raise  FileNotFoundError(f"The file {csv_path} does not exist.")
    except pd.errors.EmptyDataError:
        raise ValueError("The file is empty.")
    except pd.errors.ParserError:
        raise ValueError("The file could not be parsed. Please check the file format.")
    

 # Filtrage des lignes
    revenues = df[df['Type'].str.lower() == 'Revenue']
    depense = df[df['Type'].str.lower() == 'Dépense']

    return revenues, depense


def calculating_budget(revenues, depense):
    """
    Calculates the total budget from revenues and spending DataFrames.
    
    Args:
        revenues (pd.DataFrame): DataFrame containing revenue data.
        spending (pd.DataFrame): DataFrame containing spending data.
        
    Returns:
        float: The total budget calculated as total revenues minus total spending.
    """
    
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




