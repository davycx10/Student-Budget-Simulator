import argparse
from budget import read_budget, calculating_budget
from utils import (
    format_monnaie,
    get_month_label,
    generate_filename,
    ensure_directory_exists,
    recommendation_message


)

from matplotlib import pyplot as plt


def print_budget_summary(budget_data):

    """
    Print the budget summary.
    
    Args:
        budget_data (dict): A dictionary containing budget data.
    """
    
    print(f"\n --- Résumé du budget --- \n")

    print(f"Total Revenue: {format_monnaie(budget_data['total_revenue'])}")
    print(f"Total Dépense: {format_monnaie(budget_data['total_depense'])}")
    print(f"Reste mensuel: {format_monnaie(budget_data['reste_budget'])}")
    print(f"Taux d'épargne: {int(budget_data['taux_depense'] * 100)}%")


def print_recommendation(taux_epargne, taux_depense):

    for reco in recommendation_message(taux_epargne, taux_depense):
        print("-", reco)


def generate_graphic(depense):

    ensure_directory_exists("graphs")
    filename = generate_filename("budget_graphic", "png")

    labels = depense['Name']
    valeurs = depense['Montant']

    plt.figure(figsize=(6, 6))
    plt.pie(valeurs, labels=labels, autopct='%1.1f%%')
    plt.title("Répartition des dépenses")
    plt.savefig(f"graphs/{filename}")
    plt.close()

    print(f"\n Graphique sauvegardé dans: graphs/{filename}")



def main():

    parser = argparse.ArgumentParser(description="Simulateur de budget étudiant")
    parser.add_argument('--input', required=True, help='Chemin vers le fichier CSV du budget')
    args = parser.parse_args()

    revenus, depenses = read_budget(args.input)
    resultats = calculating_budget(revenus, depenses)

    print_budget_summary(budget_data =resultats)
    recommendation_message(resultats['taux_epargne'], resultats['taux_depense'])
    generate_graphic(depenses)

if __name__ == "__main__":
    main()