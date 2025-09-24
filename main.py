import fonction as p4

def main():
    print("=== Puissance 4 (Python) — X=rouges, O=jaunes ===")
    board = p4.create_board()
    print(p4.board_to_str(board))

if __name__ == "__main__":
    main()