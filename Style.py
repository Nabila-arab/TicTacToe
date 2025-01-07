from tkinter import ttk
def configure_styles():
    """
    Configure les styles pour l'application Tkinter.
    """
    style = ttk.Style()
    style.theme_use("clam")  # Thème

    # Style pour les étiquettes
    style.configure(
        "Custom.TLabel",
        font=("Helvetica", 14, "bold"),
        foreground="#ffffff",  # Texte blanc
        background="#1e1e30"  # Fond sombre
    )

    # Style pour les boutons
    style.configure(
        "Custom.TButton",
        font=("Helvetica", 12, "bold"),
        foreground="#ffffff",  # Texte blanc
        background="#1e1e30",  # Fond sombre
        padding=5
    )
    style.map(
        "Custom.TButton",
        background=[("active", "#1e1e30")],  # Fond sombre au survol
        foreground=[("active", "#ffffff")]  # Texte blanc au survol
    )

    # Style pour les boutons radio
    style.configure(
        "Custom.TRadiobutton",
        font=("Helvetica", 12, "bold"),
        foreground="#ffffff",  # Texte blanc
        background="#1e1e30",  # Fond sombre
        indicatorcolor="#ffffff",  # Couleur de l'indicateur (cercle)
        indicatordiameter=15,  # Diamètre de l'indicateur
        padding=(0, 0, 0, 0)  # Supprime les marges
    )

    style.map(
        "Custom.TRadiobutton",
        background=[("active", "#1e1e30")],  # Fond sombre au survol
        foreground=[("active", "#ffffff")]  # Texte blanc au survol
    )

    style.configure(
        "Custom.TFrame",
        background="#1e1e30"  # Fond sombre
    )
    return style
