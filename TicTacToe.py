import tkinter as tk
from tkinter import ttk, messagebox
from Style import configure_styles  # Importer les styles

class TicTacToe:
    def __init__(self, root, player_symbol):
        """
        Initialise la fenêtre et le plateau de jeu.
        :param root: Fenêtre principale Tkinter.
        :param player_symbol: Symbole choisi par le joueur (X ou O).
        """
        self.root = root
        self.root.title("Jeu Tic-Tac-Toe")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        # Configurer les styles
        self.style = configure_styles()

        # Variables du jeu
        self.bg_color = "#1e1e30"  # Fond sombre
        self.x_color = "#ff0000"  # Rouge vif pour les X
        self.o_color = "#00aaff"  # Bleu lumineux pour les O
        self.line_color = "#ffffff"  # Blanc pour la ligne gagnante

        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = player_symbol
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        # Label pour indiquer l'état de la partie
        self.state_turn_label = ttk.Label(
            self.root,
            text="Partie en cours",
            style="Custom.TLabel"
        )
        self.state_turn_label.pack(pady=5)

        # Canvas pour dessiner la grille et les symboles
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg=self.bg_color, highlightthickness=0)
        self.canvas.pack(pady=5)

        # Label pour indiquer le tour
        self.label_turn = ttk.Label(
            self.root,
            text=f"Tour de : {self.current_player}",
            style="Custom.TLabel"
        )
        self.label_turn.pack()

        # Label pour indiquer que la case est déja occupée
        self.state_case_label = ttk.Label(
            self.root,
            text=f"",
            font=("Helvetica", 12),
            background=self.bg_color,  # Fond sombre
            foreground="#ff0000"  # Texte rouge
        )
        self.state_case_label.pack()



        # Bouton "Nouvelle Partie"
        self.button_nouvelle_partie = ttk.Button(
            self.root,
            text="Reset Turn",
            style="Custom.TButton",
            command=self.reset_game
        )
        self.button_nouvelle_partie.pack(pady=10)

        # Dessin de la grille
        self.draw_grid()
        self.create_widgets()

    def draw_grid(self):
        """Dessine la grille sur le canvas."""
        for i in range(1, 3):
            self.canvas.create_line(0, i * 133, 400, i * 133, width=2, fill="white")
            self.canvas.create_line(i * 133, 0, i * 133, 400, width=2, fill="white")
        self.update_turn_label()
        self.update_state_turn_label("Partie en cours")

    def create_widgets(self):
        """Crée les cases cliquables et les boutons."""
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = self.canvas.create_rectangle(
                    j * 133, i * 133, (j + 1) * 133, (i + 1) * 133,
                    fill="", outline=""
                )
                self.canvas.tag_bind(self.buttons[i][j], '<Button-1>', lambda event, row=i, col=j: self.on_button_click(row, col))

    def on_button_click(self, row, col):
        """Gère les clics sur les cases."""
        if self.board[row][col] == '':
            # Réinitialise le message d'erreur s'il y en a un
            self.state_case_label.config(text="")
            self.board[row][col] = self.current_player
            x_center = col * 133 + 66
            y_center = row * 133 + 66

            # Dessiner le symbole X ou O
            if self.current_player == "X":
                self.canvas.create_text(x_center, y_center, text="X", font=("Helvetica", 48, "bold"), fill=self.x_color)
            else:
                self.canvas.create_text(x_center, y_center, text="O", font=("Helvetica", 48, "bold"), fill=self.o_color)

            winner, winning_cells = self.check_winner(self.current_player)
            if winner:
                self.draw_winning_line(winning_cells)
                self.update_state_turn_label(f"Le joueur {self.current_player} a gagné!")
            elif self.is_board_full():
                self.update_state_turn_label("Score égalité!")
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.update_turn_label()
                self.update_state_turn_label("Partie en cours")
        else:
            # Met à jour le message d'erreur si la case est déjà occupée
            self.state_case_label.config(text="Erreur : Cette case est déjà occupée!")

    def update_turn_label(self):
        """Met à jour l'étiquette pour indiquer le joueur actuel."""
        self.label_turn.config(text=f"Tour de : {self.current_player}")

    def update_state_turn_label(self, stat):
        """Met à jour l'étiquette pour indiquer l'état de la partie."""
        self.state_turn_label.config(text=stat)

    def update_state_case_label(self, stat):
        """Afficher que la case est occupée."""
        self.state_case_label.config(text=stat)


    def check_winner(self, player):
        """Vérifie si un joueur a gagné."""
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):
                return True, [(i, 0), (i, 1), (i, 2)]
            if all(self.board[j][i] == player for j in range(3)):
                return True, [(0, i), (1, i), (2, i)]

        if all(self.board[i][i] == player for i in range(3)):
            return True, [(0, 0), (1, 1), (2, 2)]
        if all(self.board[i][2 - i] == player for i in range(3)):
            return True, [(0, 2), (1, 1), (2, 0)]
        return False, []

    def draw_winning_line(self, winning_cells):
        """Dessine une ligne rouge pour indiquer les cases gagnantes."""
        start_cell = winning_cells[0]
        end_cell = winning_cells[-1]
        x1 = start_cell[1] * 133 + 66
        y1 = start_cell[0] * 133 + 66
        x2 = end_cell[1] * 133 + 66
        y2 = end_cell[0] * 133 + 66
        self.canvas.create_line(x1, y1, x2, y2, fill=self.line_color, width=5)

    def is_board_full(self):
        """Vérifie si toutes les cases sont remplies."""
        return all(self.board[i][j] != '' for i in range(3) for j in range(3))

    def reset_game(self):
        """Réinitialise le plateau pour une nouvelle partie."""
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.canvas.delete("all")
        self.draw_grid()
        self.create_widgets()
        self.current_player = "X"
        self.update_turn_label()
        self.update_state_turn_label("Nouvelle Partie")
        self.state_case_label.config(text="")  # Réinitialise le message d'erreur

