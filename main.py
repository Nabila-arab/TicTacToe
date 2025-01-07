import tkinter as tk
from Accueil import HomePage
from TicTacToe import TicTacToe

def main():
    #création de la fenetre principale
    root = tk.Tk()

#démarre le jeu apres le choid du symbole et clique sur le bouton de démarrage.
    def start_game(player_symbol):
        """Démarre le jeu en remplaçant la page d'accueil par le jeu."""
        for widget in root.winfo_children():
            widget.destroy()
        TicTacToe(root, player_symbol)

    HomePage(root, start_game)
    root.mainloop()

if __name__ == "__main__":
    main()
