import fonction as p4


def ask_column(player):
    symbol = p4.TOK[player]
    color = "rouge" if player == p4.P1 else "jaune"
    raw = input(f"Joueur {symbol} ({color}) — colonne (1-{p4.COLS}) : ").strip()
    return int(raw) - 1 if raw.isdigit() else -1

def main():
    print("=== Puissance 4 (Python) — X=rouges, O=jaunes ===")
    board = p4.create_board()
    player = p4.P1
    print(p4.board_to_str(board))

    while True:
        col = ask_column(player)
        if not p4.is_valid_col(board, col):
            print("Colonne pleine ou invalide. Choisis une autre.\n")
            continue

        p4.drop(board, col, player)
        print(p4.board_to_str(board))
 # victoire et match nul
        if p4.check_win(board, player):
            print(f"BRAVO Joueur {p4.TOK[player]} gagne ! GG Champion")
            break

        if p4.is_draw(board):
            print("Match nul. La grille est pleine.")
            break
 # Sinon on passe au joueur suivant
        player = p4.switch_player(player)

if __name__ == "__main__":
    main()