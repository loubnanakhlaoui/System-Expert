import tkinter as tk
from tkinter import messagebox

class SystemeExpert:
    def __init__(self):
        self.faits = set()  # Utilisation d'un ensemble pour éviter les doublons
        self.regles = [
            {"conditions": {"écran noir", "pas de bip au démarrage"}, "action": "problème carte mère"},
            {"conditions": {"écran noir", "bip au démarrage"}, "action": "problème carte graphique"},
            {"conditions": {"ordinateur lent", "grésillement du disque dur"}, "action": "problème disque dur"},
            {"conditions": {"ordinateur lent", "écran bleu"}, "action": "problème mémoire RAM"},
            # Ajoutez d'autres règles ici selon vos besoins
        ]

    def ajouter_panne(self, panne, causes):
        self.regles.append({"conditions": set(causes), "action": panne})

    def modifier_panne(self, ancienne_panne, nouvelle_panne, nouvelles_causes):
        for regle in self.regles:
            if regle["action"] == ancienne_panne:
                regle["action"] = nouvelle_panne
                regle["conditions"] = set(nouvelles_causes)

    def supprimer_panne(self, panne):
        self.regles = [regle for regle in self.regles if regle["action"] != panne]

    def afficher_pannes(self):
        pannes = {}
        for regle in self.regles:
            pannes[regle["action"]] = regle["conditions"]
        return pannes

    def afficher_organes_defectueux(self, symptomes):
        organes_defectueux = []
        for regle in self.regles:
            conditions = regle["conditions"]
            if conditions.issubset(symptomes):  # Utiliser la méthode issubset pour vérifier les conditions
                organes_defectueux.append(regle["action"])
        return organes_defectueux
    

class ConnexionType:
    def __init__(self, root):
        self.root = root
        self.root.title("Choix du Type de Connexion")
        
        self.label_instruction = tk.Label(root, text="Veuillez choisir le type de connexion :")
        self.label_instruction.pack()

        self.button_expert = tk.Button(root, text="Expert", command=self.connect_as_expert)
        self.button_expert.pack()

        self.button_utilisateur = tk.Button(root, text="Utilisateur", command=self.connect_as_utilisateur)
        self.button_utilisateur.pack()

    def connect_as_expert(self):
        self.root.destroy()
        expert_root = tk.Tk()
        connexion_expert = ConnexionExpert(expert_root)
        expert_root.mainloop()

    def connect_as_utilisateur(self):
        self.root.destroy()
        user_root = tk.Tk()
        connexion_utilisateur = ConnexionUtilisateur(user_root)
        user_root.mainloop()

class ConnexionExpert:
    def __init__(self, root):
        self.root = root
        self.root.title("Connexion - Expert")
        
        self.label_username = tk.Label(root, text="Nom d'utilisateur :")
        self.label_username.pack()
        
        self.entry_username = tk.Entry(root)
        self.entry_username.pack()
        
        self.label_password = tk.Label(root, text="Mot de passe :")
        self.label_password.pack()
        
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack()
        
        self.button_login = tk.Button(root, text="Connexion", command=self.login)
        self.button_login.pack()
        
        self.button_retour = tk.Button(root, text="Retour", command=self.retour)
        self.button_retour.pack()

        self.button_ajouter_expert = tk.Button(root, text="Ajouter un Expert", command=self.ajouter_expert)
        self.button_ajouter_expert.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Vérifiez ici les informations de connexion pour l'expert
        if self.verify_user_credentials(username, password):
            self.root.destroy()
            ExpertApplication()

        else:
            messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect.")
            
    def retour(self):
        self.root.destroy()
        root = tk.Tk()
        connexion_type = ConnexionType(root)
        root.mainloop()
        
    def verify_user_credentials(self, username, password):
        with open("experts.txt", "r") as f:
            for line in f:
                stored_username, stored_password = line.strip().split(",")
                if username == stored_username and password == stored_password:
                    return True
        return False    

    def ajouter_expert(self):
        ajout_expert_window = tk.Toplevel(self.root)
        ajout_expert_window.title("Ajouter Expert")

        label_username = tk.Label(ajout_expert_window, text="Nom d'utilisateur :")
        label_username.pack()

        entry_username = tk.Entry(ajout_expert_window)
        entry_username.pack()

        label_password = tk.Label(ajout_expert_window, text="Mot de passe :")
        label_password.pack()

        entry_password = tk.Entry(ajout_expert_window, show="*")
        entry_password.pack()

        button_valider = tk.Button(ajout_expert_window, text="Valider", command=lambda: self.valider_ajout_expert(entry_username.get(), entry_password.get(), ajout_expert_window))
        button_valider.pack()

    def valider_ajout_expert(self, username, password, ajout_expert_window):
        with open("experts.txt", "a") as f:
            f.write(f"{username},{password}\n")
        ajout_expert_window.destroy()
        messagebox.showinfo("Expert ajouté", "Expert ajouté avec succès.")

class ConnexionUtilisateur:
    def __init__(self, root):
        self.root = root
        self.root.title("Connexion - Utilisateur")
        
        self.label_username = tk.Label(root, text="Nom d'utilisateur :")
        self.label_username.pack()
        
        self.entry_username = tk.Entry(root)
        self.entry_username.pack()
        
        self.label_password = tk.Label(root, text="Mot de passe :")
        self.label_password.pack()
        
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack()
        
        self.button_login = tk.Button(root, text="Connexion", command=self.login)
        self.button_login.pack()
        
        self.button_retour = tk.Button(self.root, text="Retour", command=self.retour)
        self.button_retour.pack()

        self.button_ajouter_utilisateur = tk.Button(root, text="Ajouter un Utilisateur", command=self.ajouter_utilisateur)
        self.button_ajouter_utilisateur.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Vérifiez ici les informations de connexion pour l'utilisateur
        if self.verify_user_credentials(username, password):
            self.root.destroy()
            UtilisateurApplication()
        else:
            messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe")
            
    def retour(self):
        self.root.destroy()
        root = tk.Tk()
        connexion_type = ConnexionType(root)
        root.mainloop()

    def verify_user_credentials(self, username, password):
        with open("utilisateurs.txt", "r") as f:
            for line in f:
                stored_username, stored_password = line.strip().split(",")
                if username == stored_username and password == stored_password:
                    return True
        return False

    def ajouter_utilisateur(self):
        ajout_utilisateur_window = tk.Toplevel(self.root)
        ajout_utilisateur_window.title("Ajouter Utilisateur")

        label_username = tk.Label(ajout_utilisateur_window, text="Nom d'utilisateur :")
        label_username.pack()

        entry_username = tk.Entry(ajout_utilisateur_window)
        entry_username.pack()

        label_password = tk.Label(ajout_utilisateur_window, text="Mot de passe :")
        label_password.pack()

        entry_password = tk.Entry(ajout_utilisateur_window, show="*")
        entry_password.pack()

        button_valider = tk.Button(ajout_utilisateur_window, text="Valider", command=lambda: self.valider_ajout_utilisateur(entry_username.get(), entry_password.get(), ajout_utilisateur_window))
        button_valider.pack()

    def valider_ajout_utilisateur(self, username, password, ajout_utilisateur_window):
        with open("utilisateurs.txt", "a") as f:
            f.write(f"{username},{password}\n")
        ajout_utilisateur_window.destroy()
        messagebox.showinfo("Utilisateur ajouté", "Utilisateur ajouté avec succès.")

class UtilisateurApplication:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Système Expert - Mode Utilisateur")

        self.systeme = SystemeExpert()

        self.label_instructions = tk.Label(self.root, text="Veuillez sélectionner les symptômes observés :")
        self.label_instructions.pack()

        # Ajout de boutons pour les symptômes
        self.symptomes_frame = tk.Frame(self.root)
        self.symptomes_frame.pack()

        self.symptomes = [
            "écran noir",
            "pas de bip au démarrage",
            "bip au démarrage",
            "ordinateur lent",
            "grésillement du disque dur",
            "écran bleu"
        ]

        self.symptomes_selectionnes = []

        for symptome in self.symptomes:
            symptome_button = tk.Button(self.symptomes_frame, text=symptome, command=lambda s=symptome: self.toggle_symptome(s))
            symptome_button.pack(side=tk.LEFT)

        self.bouton_soumettre = tk.Button(self.root, text="Soumettre", command=self.soumettre_symptomes)
        self.bouton_soumettre.pack()

        self.resultat = tk.Label(self.root, text="")
        self.resultat.pack()
        
        self.bouton_reset = tk.Button(self.root, text="Réinitialiser", command=self.reset_selection)
        self.bouton_reset.pack()
        
               
        self.button_retour = tk.Button(self.root, text="Retour", command=self.retour)
        self.button_retour.pack()  

    def toggle_symptome(self, symptome):
        if symptome in self.symptomes_selectionnes:
            self.symptomes_selectionnes.remove(symptome)
        else:
            self.symptomes_selectionnes.append(symptome)

    def soumettre_symptomes(self):
        organes_defectueux = self.systeme.afficher_organes_defectueux(self.symptomes_selectionnes)
        if organes_defectueux:
            self.resultat.config(text=f"Les organes susceptibles d'être défectueux sont : {', '.join(organes_defectueux)}")
        else:
            self.resultat.config(text="Aucun organe défectueux trouvé pour les symptômes sélectionnés.")
            
    def reset_selection(self):
        self.symptomes_selectionnes.clear()  # Réinitialise la liste des symptômes sélectionnés
        self.resultat.config(text="")  # Efface le résultat précédent  
        
    def retour(self):
        self.root.destroy()
        root = tk.Tk()
        connexion_type = ConnexionType(root)
        root.mainloop()    

class ExpertApplication:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Système Expert - Mode Expert")

        self.systeme = SystemeExpert()

        self.label_instructions = tk.Label(self.root, text="Bienvenue, expert. Que souhaitez-vous faire?")
        self.label_instructions.pack()

        self.button_afficher_pannes = tk.Button(self.root, text="Afficher les pannes", command=self.afficher_pannes)
        self.button_afficher_pannes.pack()

        self.button_ajouter_panne = tk.Button(self.root, text="Ajouter une panne", command=self.ajouter_panne)
        self.button_ajouter_panne.pack()

        self.button_modifier_panne = tk.Button(self.root, text="Modifier une panne", command=self.modifier_panne)
        self.button_modifier_panne.pack()

        self.button_supprimer_panne = tk.Button(self.root, text="Supprimer une panne", command=self.supprimer_panne)
        self.button_supprimer_panne.pack()
        
        self.button_retour = tk.Button(self.root, text="Retour", command=self.retour)
        self.button_retour.pack()  
        
        
    def ajouter_panne(self):
        ajout_panne_window = tk.Toplevel(self.root)
        ajout_panne_window.title("Ajouter Panne")

        label_panne = tk.Label(ajout_panne_window, text="Nom de la panne :")
        label_panne.pack()

        entry_panne = tk.Entry(ajout_panne_window)
        entry_panne.pack()

        label_causes = tk.Label(ajout_panne_window, text="Causes (séparées par des virgules) :")
        label_causes.pack()

        entry_causes = tk.Entry(ajout_panne_window)
        entry_causes.pack()

        button_valider = tk.Button(ajout_panne_window, text="Valider", command=lambda: self.valider_ajout_panne(entry_panne.get(), entry_causes.get(), ajout_panne_window))
        button_valider.pack()

    def valider_ajout_panne(self, panne, causes, ajout_panne_window):
        causes_liste = [cause.strip() for cause in causes.split(",")]
        self.systeme.ajouter_panne(panne, causes_liste)
        ajout_panne_window.destroy()  
        self.afficher_pannes()  
        messagebox.showinfo("Panne ajoutée", f"La panne '{panne}' a été ajoutée avec succès.")

    def modifier_panne(self):
        modification_panne_window = tk.Toplevel(self.root)
        modification_panne_window.title("Modifier Panne")

        label_ancienne_panne = tk.Label(modification_panne_window, text="Ancien nom de la panne :")
        label_ancienne_panne.pack()

        entry_ancienne_panne = tk.Entry(modification_panne_window)
        entry_ancienne_panne.pack()

        label_nouvelle_panne = tk.Label(modification_panne_window, text="Nouveau nom de la panne :")
        label_nouvelle_panne.pack()

        entry_nouvelle_panne = tk.Entry(modification_panne_window)
        entry_nouvelle_panne.pack()

        label_nouvelles_causes = tk.Label(modification_panne_window, text="Nouvelles causes (séparées par des virgules) :")
        label_nouvelles_causes.pack()

        entry_nouvelles_causes = tk.Entry(modification_panne_window)
        entry_nouvelles_causes.pack()

        button_valider = tk.Button(modification_panne_window, text="Valider", command=lambda: self.valider_modification_panne(entry_ancienne_panne.get(), entry_nouvelle_panne.get(), entry_nouvelles_causes.get(), modification_panne_window))
        button_valider.pack()

    def valider_modification_panne(self, ancienne_panne, nouvelle_panne, nouvelles_causes, modification_panne_window):
        nouvelles_causes_liste = [cause.strip() for cause in nouvelles_causes.split(",")]
        self.systeme.modifier_panne(ancienne_panne, nouvelle_panne, nouvelles_causes_liste)
        modification_panne_window.destroy()  
        self.afficher_pannes()  
        messagebox.showinfo("Panne modifiée", f"La panne '{ancienne_panne}' a été modifiée en '{nouvelle_panne}' avec les nouvelles causes '{', '.join(nouvelles_causes_liste)}'.")

    def supprimer_panne(self):
        suppression_panne_window = tk.Toplevel(self.root)
        suppression_panne_window.title("Supprimer Panne")

        label_panne = tk.Label(suppression_panne_window, text="Nom de la panne à supprimer :")
        label_panne.pack()

        entry_panne = tk.Entry(suppression_panne_window)
        entry_panne.pack()

        button_valider = tk.Button(suppression_panne_window, text="Valider", command=lambda: self.valider_suppression_panne(entry_panne.get(), suppression_panne_window))
        button_valider.pack()

    def valider_suppression_panne(self, panne, suppression_panne_window):
        self.systeme.supprimer_panne(panne)
        suppression_panne_window.destroy()  
        self.afficher_pannes()  
        messagebox.showinfo("Panne supprimée", f"La panne '{panne}' a été supprimée avec succès.")

    def afficher_pannes(self):
        for widget in self.root.winfo_children():
            if widget not in [self.button_ajouter_panne, self.button_modifier_panne, self.button_supprimer_panne]:
                widget.destroy()

        pannes = self.systeme.afficher_pannes()
        for panne, causes in pannes.items():
            label_panne = tk.Label(self.root, text=f"Panne: {panne}, Causes: {', '.join(causes)}")
            label_panne.pack()
            
        self.button_retour = tk.Button(self.root, text="Retour", command=self.retour)
        self.button_retour.pack()   
            
    def retour(self):
        self.root.destroy()
        root = tk.Tk()
        connexion_type = ConnexionType(root)
        root.mainloop() 

root = tk.Tk()
connexion_type = ConnexionType(root)
root.mainloop()
