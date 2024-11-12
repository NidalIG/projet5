import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
# Charger les données
df = pd.read_csv("epa-sea-level.csv")

# Afficher les 5 premières lignes pour examiner les données
print(df.head())
def draw_plot():
    # Créer la figure
    plt.figure(figsize=(10, 5))
    
    # Graphique en dispersion
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data Points')

    # Titre et labels
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    # Calculer la ligne de meilleure régression pour les données de 1880 à 2050
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Créer des années pour la prédiction
    years_extended = pd.Series([i for i in range(1880, 2051)])
    
    # Calculer les valeurs prédites
    sea_level_pred = intercept + slope * years_extended
    
    # Tracer la ligne de meilleure régression
    plt.plot(years_extended, sea_level_pred, color='red', label='Best Fit Line (1880-2050)')
    # Filtrer les données depuis l'an 2000
    df_recent = df[df['Year'] >= 2000]
    
    # Calculer la ligne de meilleure régression pour les données de 2000 à 2050
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Calculer les valeurs prédites
    sea_level_pred_recent = intercept_recent + slope_recent * years_extended
    
    # Tracer la ligne de meilleure régression
    plt.plot(years_extended, sea_level_pred_recent, color='green', label='Best Fit Line (2000-2050)')
    # Ajouter la légende
    plt.legend()

    # Sauvegarder l'image
    plt.savefig('sea_level_plot.png')
    
    # Retourner la figure pour les tests
    return plt.gca()
