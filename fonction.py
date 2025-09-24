ROWS, COLS = 6, 7
EMPTY, P1, P2 = 0, 1, 2
TOK = {EMPTY: ".", P1: "X", P2: "O"}  # X=rouges, O=jaunes


def create_board():
    """Crée une grille 6x7 vide (valeurs 0)."""
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def board_to_str(board):
    """Retourne un rendu ASCII de la grille."""
    lines = []
    lines.append("  " + " ".join(str(i) for i in range(1, COLS + 1)))
    for r in range(ROWS):
        lines.append("| " + " ".join(TOK[board[r][c]] for c in range(COLS)) + " |")
    lines.append("+" + "--" * COLS + "-+")
    return "\n".join(lines)