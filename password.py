#créer des interfaces graphiques (fenêtres, boutons, champs de texte)
import tkinter as tk
#afficher des boîtes de dialogue (alertes, confirmations, messages d’erreur)
from tkinter import messagebox
#Fournit des fonctions pour chiffrer et déchiffrer des données
from cryptography.fernet import Fernet
#interagir avec le système d’exploitation fichiers, dossiers, chemins, variables d’environnement
import os
#lire et écrire des données au format JSON pour le stockage ou l’échange d’informations
import json

# ---------------- 1- Key generation and encryption setup ----------------
# d'abord en commence par creer notre cle de chifferement , on va generer un cle qui sera utiliser pour crypter (chiffrer) le password
def generate_key():
    """c la fonction qui gener ce cle"""
    return Fernet.generate_key()

# avant d'utiliser cette fonction on verifier c il existe deja un fichier qui contien un cle de chiffrement
def load_key():
    """
    cette fonction verifier si il existe la cle avant
    rb : veut dire lire un fichier binaire
    else in case there is no key 
    genere la cle de chiffrement 
    wb : write binary , ecrire binaire
    """
    if os.path.exists(secret.key):
        with open("secrect.key", "rb") as key_file:
            return key_file.read()
    else:
        key = generate_key()
        with open("secret.key","wb") as key_file:
            key_file.write(key)
        return key
#chifrement / dechiffrement du message il ce fait par le library cryptography 
#1- chiffrement un message 
def encrypt_message(message,key):
    """ cree un objet de Fernet pour le chiffrement en utilisant key
    convertir le text en byte car le chiffrement ce fait par une cle en binaire
    .encrypt() pour le chiffrement
    """
    f = Fernet(key)
    return f.encrypt(message.encode())
#2-dechiffrement message
def decrypt_message(encrypted_message , key):
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()

# Appelle load_key() pour obtenir une clé de chiffrement
key = load_key()


# ---------------- Application functions ----------------

def save_password():
    """ collecte user input , encrypt passsword , stor it in jason file """
    """ GUI input fields """ 
    service = service_entry.get()
    username = username_entry.get()
    password = password_entry.get()

   if not service or not username or not password:
      messagebox.showwarning("Input Error", "Please fill all fields.")
      return
       
       
   encrypted_password = encrypt_message(password, key) 
   new_data = {service: {"username": username, "password": encrypted_password.decode()}}

   if os.path.exists("password.json"):
       with open("password.json", "r") as file : 
           try:
               existing_data = json.load(file)
           except (json.JSONDecodeError, TypeError):
               existing_data = {}
        existing_data.update(new_data)
    else : 
        existing_data = new_data

        

       

           
   

    









