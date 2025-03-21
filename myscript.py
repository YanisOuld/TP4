import os

# Remplacez ces variables avec les bons hachages
good_hash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"
bad_hash = "c1a4be04b972b6c17db242fc37752ad517c29402"

# Exécution de git bisect pour démarrer
os.system(f"git bisect start {bad_hash} {good_hash}")

# Utilisation de git bisect run pour exécuter les tests sur chaque commit
# Remplacer "pytest" par la commande qui exécute les tests dans ton projet
os.system("git bisect run py manage.py test")

# Réinitialisation de git bisect à la fin du processus
os.system("git bisect reset")