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
        if not {'Type', 'Name','Amount' }.issubset(df.columns):
            raise Exception('The budget file is not in the correct format. It must contain Type, Name, and Amount columns.')
        
    except FileNotFoundError:
        raise  FileNotFoundError(f"The file {csv_path} does not exist.")
    except pd.errors.EmptyDataError:
        raise ValueError("The file is empty.")
    except pd.errors.ParserError:
        raise ValueError("The file could not be parsed. Please check the file format.")
    

 # Filtrage des lignes
    revenues = df[df['Type'].str.lower() == 'Revenue']
    spending = df[df['Type'].str.lower() == 'Spending']

    return revenues, spending
    
