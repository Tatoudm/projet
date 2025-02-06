import time
import subprocess

def run_command(command):
    """Exécute une commande shell et affiche la sortie."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

def check_github_auth():
    """Vérifie si l'utilisateur est authentifié sur GitHub."""
    result = subprocess.run("git config --global user.name", shell=True, capture_output=True, text=True)
    username = result.stdout.strip()
    if not username:
        print("Aucun utilisateur GitHub configuré. Veuillez vous connecter.")
        username = input("Entrez votre nom d'utilisateur GitHub: ")
        email = input("Entrez votre email GitHub: ")
        run_command(f"git config --global user.name '{username}'")
        run_command(f"git config --global user.email '{email}'")
        print("GitHub configuré avec succès.")
    return username

def check_git_remote():
    """Vérifie si un dépôt Git est configuré, sinon configure celui par défaut."""
    result = subprocess.run("git remote get-url origin", shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print("Aucun dépôt Git configuré. Configuration du dépôt par défaut...")
        run_command("git remote add origin https://github.com/tatoudm/projet.git")
        run_command("git branch -M main")
        run_command("git push -u origin main")
    else:
        print("Dépôt Git déjà configuré.")

def git_sync():
    username = check_github_auth()
    check_git_remote()
    while True:
        print("\n--- Synchronisation Git en cours ---")
        run_command("git pull --rebase")
        time.sleep(2)  # Petite pause après le pull
        run_command("git add -A")
        run_command(f"git commit -m '{username}'")
        run_command("git push --set-upstream origin main")
        print("\n--- Synchronisation terminée. Attente avant le prochain cycle... ---")
        time.sleep(60)  # Attente de 60 secondes avant la prochaine synchronisation

if __name__ == "__main__":
    git_sync()
