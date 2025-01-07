import tkinter as tk
from tkinter import ttk
from Style import configure_styles  # Importer les styles

class HomePage:
    def __init__(self, root, start_game_callback):
        """
        Initialise la page d'accueil.
        :param root: Fenêtre principale Tkinter.
        :param start_game_callback: Fonction appelée pour démarrer le jeu.
        """
        self.root = root
        self.start_game_callback = start_game_callback
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("500x450")
        self.root.configure(bg="#1e1e30")  # Fond sombre

        # # Appelle la fonction pour Configurer les styles
        self.style = configure_styles()

        # Création d'un label pour le titre principal avec un style personnalisé
        ttk.Label(
            self.root,
            text="Bienvenue dans Tic-Tac-Toe!",
            style="Custom.TLabel"
        ).pack(pady=25)

        # Choix du symbole
        ttk.Label(
            self.root,
            text="Choisissez votre symbole:",
            style="Custom.TLabel"
        ).pack(pady=50)

        # Frame invisible pour aligner les boutons radio horizontalement
        radio_frame = ttk.Frame(self.root, style="Custom.TFrame")
        radio_frame.pack(pady=20)

        # Variable pour stocker le symbole choisi
        self.symbol_choice = tk.StringVar(value="X")  # Par défaut, X est sélectionné

        # Boutons radio pour choisir X ou O
        ttk.Radiobutton(
            radio_frame,
            text="X",
            variable=self.symbol_choice,
            value="X",
            style="Custom.TRadiobutton"
        ).pack(side=tk.LEFT, padx=10)

        ttk.Radiobutton(
            radio_frame,
            text="O",
            variable=self.symbol_choice,
            value="O",
            style="Custom.TRadiobutton"
        ).pack(side=tk.LEFT, padx=10)

        # Bouton pour démarrer le jeu
        ttk.Button(
            self.root,
            text="Démarrer le jeu",
            style="Custom.TButton",
            command=self.start_game
        ).pack(pady=20)

    def start_game(self):
        """Appelé lorsqu'on clique sur 'Démarrer le jeu'."""
        symbol = self.symbol_choice.get()
        self.start_game_callback(symbol)
