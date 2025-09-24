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

def is_valid_col(board, col):
    """True si 0 <= col < COLS et si la case du haut est vide."""
    return 0 <= col < COLS and board[0][col] == EMPTY

def drop(board, col, player):
    """Fait tomber le pion dans la colonne."""
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == EMPTY:
            board[r][col] = player
            return r, col
    return None

def check_win(board, player):
    """Vérifié les 4 alignés (horizontal)"""
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c + i] == player for i in range(4)):
                return True
            # Vertical
    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r + i][c] == player for i in range(4)):
                return True
    # Diagonale
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == player for i in range(4)):
                return True
    # Diagonale
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r - i][c + i] == player for i in range(4)):
                return True
    return False

def is_draw(board):
    return all(board[0][c] != EMPTY for c in range(COLS))

def switch_player(p):
    return P2 if p == P1 else P1
