import socket # Bibliothèque pour les communications réseau
import sys    # Pour pouvoir quitter le programme proprement

# --- 1. CONFIGURATION ET RÉSOLUTION D'ADRESSE ---

# On demande à l'utilisateur de saisir une cible (ex: google.com ou 127.0.0.1)
nom_cible = input("Entrez le nom du site ou l'IP à scanner (ex; google.com ou 127.0.0.1 ): ")

try:
    # On transforme le nom (ex: google.com) en adresse IP (ex: 142.250...)
    # C'est ce qu'on appelle la résolution DNS
    target = socket.gethostbyname(nom_cible)
    print(f"\n[!] Cible convertie en IP : {target}")
except socket.gaierror:
    # Si l'utilisateur tape n'importe quoi ou n'a pas internet
    print("\n[X] Erreur : Impossible de trouver l'adresse. Vérifiez votre saisie.")
    sys.exit()

# --- 2. DICTIONNAIRE DES SERVICES ---

# On crée un annuaire pour savoir à quoi sert chaque port trouvé ouvert
services_connus = {
    21: "FTP (Transfert de fichiers)",
    22: "SSH (Connexion sécurisée)",
    23: "Telnet (Vieux protocole non sécurisé)",
    25: "SMTP (Envoi d'emails)",
    80: "HTTP (Site Web)",
    135: "RPC (Service Windows)",
    443: "HTTPS (Site Web sécurisé)",
    445: "SMB (Partage de fichiers Windows)",
    3306: "MySQL (Base de données)"
}

# --- 3. LA FONCTION DE SCAN ---

def scan_port(port):
    # On crée une 'socket' (un point de connexion)
    # AF_INET = IPv4 | SOCK_STREAM = protocole TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # On définit un temps d'attente court pour ne pas attendre des heures
    s.settimeout(0.5) 
    
    # On tente la connexion. connect_ex renvoie 0 si ça marche
    resultat = s.connect_ex((target, port))
    
    if resultat == 0:
        # On verifie si on connaît le service dans notre dictionnaire
        # Si le port n'est pas dans le dictio, on affiche "Service inconnu"
        nom_service = services_connus.get(port, "Service inconnu")
        print(f" [+] Port {port} : OUVERT | {nom_service}")
    
    # On referme la socket pour libérer les ressources de l'ordinateur
    s.close()

# --- 4. LANCEMENT DU SCAN ---

print(f"--- Début du scan sur {nom_cible} ---")
print("Cela peut prendre une minute...\n")

# On lance la boucle de 1 à 1024 (les ports les plus importants)
for p in range(1, 1025):
    scan_port(p)

print("\n--- Scan terminé avec succès! ---")