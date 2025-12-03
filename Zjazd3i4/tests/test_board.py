import random
import pytest

from game.board import Board, Direction, Position, CellType


def test_board_min_size():
    board = Board(5, 5, obstacle_probability=0.0, rng=random.Random(0))
    assert board.rows == 5
    assert board.cols == 5


def test_start_and_stop_on_edge_and_not_adjacent():
    board = Board(7, 10, obstacle_probability=0.0, rng=random.Random(1))
    start = board.start
    stop = board.stop

    # START i STOP na krawędzi
    def is_edge(p: Position) -> bool:
        return p.row in (0, board.rows - 1) or p.col in (0, board.cols - 1)

    assert is_edge(start)
    assert is_edge(stop)

    assert start != stop

    # nie sąsiadują 4-kierunkowo
    dr = abs(start.row - stop.row)
    dc = abs(start.col - stop.col)
    assert not ((dr == 1 and dc == 0) or (dr == 0 and dc == 1))


def test_obstacles_not_on_start_or_stop():
    board = Board(6, 6, obstacle_probability=0.5, rng=random.Random(2))

    assert board.grid[board.start.row][board.start.col] == CellType.START
    assert board.grid[board.stop.row][board.stop.col] == CellType.STOP

    # upewniamy się, że nigdzie start/stop nie zostały nadpisane przeszkodą
    assert board.grid[board.start.row][board.start.col] != CellType.OBSTACLE
    assert board.grid[board.stop.row][board.stop.col] != CellType.OBSTACLE


def test_cannot_move_outside_board():
    # wymuszony start w rogu poprzez niski rozmiar + brak przeszkód
    board = Board(5, 5, obstacle_probability=0.0, rng=random.Random(3))
    start = board.start
    board.current = start

    # jeśli start w górnym rzędzie, ruch w górę niedozwolony
    if start.row == 0:
        assert board.can_move(Direction.UP) is False
        assert board.move(Direction.UP) is False

    # jeśli start w lewej kolumnie, ruch w lewo niedozwolony
    if start.col == 0:
        assert board.can_move(Direction.LEFT) is False
        assert board.move(Direction.LEFT) is False


def test_cannot_move_into_obstacle():
    # mała plansza, wstawiamy przeszkodę obok aktualnej pozycji
    board = Board(5, 5, obstacle_probability=0.0, rng=random.Random(4))

    # ustawiamy current na (2,2) jeśli się da, inaczej na start
    pos = Position(2, 2)
    if board.is_inside(pos):
        board.current = pos
    else:
        board.current = board.start
        pos = board.current

    # wybieramy kierunek w prawo, jeśli jest w planszy
    target = Position(pos.row, pos.col + 1)
    if board.is_inside(target):
        board.grid[target.row][target.col] = CellType.OBSTACLE
        assert board.can_move(Direction.RIGHT) is False
        assert board.move(Direction.RIGHT) is False


def test_successful_move():
    board = Board(5, 5, obstacle_probability=0.0, rng=random.Random(5))

    # wybieramy pozycję, z której da się pójść w dół
    start = Position(1, 1)
    assert board.is_inside(start)
    board.current = start

    target = Position(start.row + 1, start.col)
    assert board.is_inside(target)
    assert not board.is_obstacle(target)

    assert board.can_move(Direction.DOWN) is True
    moved = board.move(Direction.DOWN)
    assert moved is True
    assert board.current == target


def test_to_string_contains_start_and_stop():
    board = Board(5, 5, obstacle_probability=0.0, rng=random.Random(6))
    s = board.to_string()
    assert "A" in s
    assert "B" in s
