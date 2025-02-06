import time
import subprocess

def run_command(command):
    """Exécute une commande shell et affiche la sortie."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

def git_sync():
    while True:
        print("\n--- Synchronisation Git en cours ---")
        run_command("git pull")
        time.sleep(2)  # Petite pause après le pull
        run_command("git add .")
        run_command("git commit -m Victor")
        run_command("git push")
        print("\n--- Synchronisation terminée. Attente avant le prochain cycle... ---")
        time.sleep(60)  

if __name__ == "__main__":
    git_sync()