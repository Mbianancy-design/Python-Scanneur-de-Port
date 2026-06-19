# 🔍 Scanner de Ports en Python

Outil de scan de ports réseau développé en Python, permettant de détecter les ports ouverts sur une machine ou une adresse IP afin d'identifier les services exposés et les vulnérabilités potentielles.

## 📌 Description

Ce script analyse une plage de ports sur une cible donnée (adresse IP ou nom de domaine) et indique lesquels sont ouverts, fermés ou filtrés. Il s'inscrit dans une démarche d'apprentissage de la cybersécurité, en lien avec mon Google Cybersecurity Professional Certificate.

## ⚙️ Fonctionnalités

- Scan d'un port unique ou d'une plage de ports (ex: 1-1024)
- Détection des ports ouverts / fermés
- Identification du service associé à un port connu (ex: 80 → HTTP, 443 → HTTPS, 22 → SSH)
- Mesure du temps de réponse du scan
- Gestion des erreurs (hôte injoignable, timeout réseau)
- Affichage clair des résultats dans le terminal

## 🛠️ Technologies utilisées

- Python 3
- Module `socket` (connexions réseau bas niveau)
- SYN-ACK (Synchronization -Acknowledge)

## 🚀 Utilisation

```bash
python ports_scanner2.py
```

Puis suis les instructions à l'écran pour entrer l'IP/nom d'hôte cible et la plage de ports à scanner.

*(Adapte cette partie selon comment ton-ACK script demande réellement les inputs)*

## 📋 Exemple de résultat


## ⚠️ Avertissement

Ce script est destiné à un usage **pédagogique et éthique uniquement** : scan de vos propres machines ou réseaux, ou environnements pour lesquels vous avez une autorisation explicite. Le scan de systèmes tiers sans autorisation est illégal.

## 📚 Ce que ce projet m'a appris

- Fonctionnement des connexions TCP/IP et des sockets
- Identification des services réseau exposés
- Notions fondamentales de reconnaissance réseau en cybersécurité

## 👤 Auteur

Ahanda Nancy — Étudiante en BTS Informatique
