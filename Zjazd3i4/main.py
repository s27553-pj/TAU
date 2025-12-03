from game.board import Board, Direction

def main():
    # Tworzymy planszę 8x8 z przeszkodami
    board = Board(8, 8, obstacle_probability=0.2)

    print("=== PLANSZA STARTOWA ===")
    print(board.to_string())

    print("\nSTART: A, STOP: B, przeszkody: X, puste: . , aktualna pozycja może być '@'")
    print("Sterowanie:")
    print("  w - góra")
    print("  s - dół")
    print("  a - lewo")
    print("  d - prawo")
    print("  q - wyjście")

    while True:
        key = input("Ruch (w/a/s/d/q): ").strip().lower()

        if key == "q":
            print("Zakończono grę.")
            break

        direction = {
            "w": Direction.UP,
            "s": Direction.DOWN,
            "a": Direction.LEFT,
            "d": Direction.RIGHT
        }.get(key)

        if direction is None:
            print("Nieznane polecenie!")
            continue

        if board.move(direction):
            print("\nOK — ruch wykonany")
        else:
            print("\nRuch niemożliwy!")

        print(board.to_string())

        # wygrana
        if board.current == board.stop:
            print("\n GRATULACJE — dotarłeś do celu!")
            break


if __name__ == "__main__":
    main()
