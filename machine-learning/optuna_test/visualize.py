import optuna
import matplotlib.pyplot as plt

# Charger l'étude
study = optuna.load_study(
    study_name='breast_cancer_optimization',
    storage='sqlite:///optuna_study.db'
)

# 1. Historique d'optimisation
fig1 = optuna.visualization.matplotlib.plot_optimization_history(study)
plt.title("Historique d'Optimisation")
plt.tight_layout()
plt.savefig('optimization_history.png')
plt.close()

# 2. Importance des paramètres
fig2 = optuna.visualization.matplotlib.plot_param_importances(study)
plt.title("Importance des Paramètres")
plt.tight_layout()
plt.savefig('param_importances.png')
plt.close()

# 3. Graphique de contour
fig3 = optuna.visualization.matplotlib.plot_contour(study)
plt.tight_layout()
plt.savefig('contour_plot.png')
plt.close()

print("Visualisations sauvegardées :")
print("- optimization_history.png")
print("- param_importances.png")
print("- contour_plot.png")

