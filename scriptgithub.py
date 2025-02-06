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
    if not result.stdout.strip():
        print("Aucun utilisateur GitHub configuré. Veuillez vous connecter.")
        username = input("Entrez votre nom d'utilisateur GitHub: ")
        email = input("Entrez votre email GitHub: ")
        run_command(f"git config --global user.name '{username}'")
        run_command(f"git config --global user.email '{email}'")
        print("GitHub configuré avec succès.")

def git_sync():
    check_github_auth()
    while True:
        print("\n--- Synchronisation Git en cours ---")
        run_command("git pull")
        time.sleep(2)  
        run_command("git add .")
        run_command("git commit -m Nathan")
        run_command("git push")
        print("\n--- Synchronisation terminée. Attente avant le prochain cycle... ---")
        time.sleep(60) 

if __name__ == "__main__":
    git_sync()