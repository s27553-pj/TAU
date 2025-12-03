from dataclasses import dataclass
from enum import Enum, auto
import random
from typing import List, Tuple, Optional


class CellType(Enum):
    EMPTY = auto()
    START = auto()
    STOP = auto()
    OBSTACLE = auto()


@dataclass(frozen=True)
class Position:
    row: int
    col: int


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


class Board:
    """
    Logika gry:
    - generowanie planszy AxB
    - losowanie START/STOP na krawędzi
    - losowe przeszkody
    - walidacja ruchu i wykonywanie ruchu
    """

    def __init__(
        self,
        rows: int,
        cols: int,
        obstacle_probability: float = 0.2,
        rng: Optional[random.Random] = None,
    ):
        if rows < 5 or cols < 5:
            raise ValueError("Minimalny rozmiar planszy to 5x5")
        if not (0.0 <= obstacle_probability <= 1.0):
            raise ValueError("Prawdopodobieństwo przeszkód musi być w zakresie [0, 1]")

        self.rows = rows
        self.cols = cols
        self.obstacle_probability = obstacle_probability
        self.rng = rng or random.Random()

        self.grid: List[List[CellType]] = [
            [CellType.EMPTY for _ in range(cols)] for _ in range(rows)
        ]

        self.start: Position
        self.stop: Position
        self.current: Position  # aktualna pozycja

        self._generate_board()

    # -------------------
    # GENEROWANIE PLANSZY
    # -------------------

    def _generate_board(self) -> None:
        self._place_start_and_stop()
        self._place_obstacles()
        # Gracz startuje na polu START
        self.current = self.start

    def _get_all_edge_positions(self) -> List[Position]:
        positions = []

        # Górny i dolny rząd
        for c in range(self.cols):
            positions.append(Position(0, c))
            positions.append(Position(self.rows - 1, c))

        # Lewa i prawa kolumna
        for r in range(1, self.rows - 1):
            positions.append(Position(r, 0))
            positions.append(Position(r, self.cols - 1))

        # Usuwanie duplikatów
        unique = list({(p.row, p.col): p for p in positions}.values())
        return unique

    def _are_adjacent(self, p1: Position, p2: Position) -> bool:
        """
        Sąsiedztwo 4-kierunkowe (góra, dół, lewo, prawo).
        """
        dr = abs(p1.row - p2.row)
        dc = abs(p1.col - p2.col)
        return (dr == 1 and dc == 0) or (dr == 0 and dc == 1)

    def _place_start_and_stop(self) -> None:
        edges = self._get_all_edge_positions()
        if len(edges) < 2:

            raise RuntimeError("Za mało pól brzegowych aby umieścić START i STOP")

        # losujemy START i STOP:
        #
        while True:
            start = self.rng.choice(edges)
            stop = self.rng.choice(edges)
            if start != stop and not self._are_adjacent(start, stop):
                break

        self.start = start
        self.stop = stop

        self.grid[start.row][start.col] = CellType.START
        self.grid[stop.row][stop.col] = CellType.STOP

    def _place_obstacles(self) -> None:
        """
        Losowo rozkładamy przeszkody X po planszy, z wyłączeniem pól START/STOP.
        """
        for r in range(self.rows):
            for c in range(self.cols):
                pos = Position(r, c)
                if pos == self.start or pos == self.stop:
                    continue
                if self.rng.random() < self.obstacle_probability:
                    self.grid[r][c] = CellType.OBSTACLE

    # -------------------
    # RUCH I WALIDACJA
    # -------------------

    def _direction_delta(self, direction: Direction) -> Tuple[int, int]:
        if direction == Direction.UP:
            return -1, 0
        if direction == Direction.DOWN:
            return 1, 0
        if direction == Direction.LEFT:
            return 0, -1
        if direction == Direction.RIGHT:
            return 0, 1
        raise ValueError("Nieznany kierunek")

    def is_inside(self, pos: Position) -> bool:
        return 0 <= pos.row < self.rows and 0 <= pos.col < self.cols

    def is_obstacle(self, pos: Position) -> bool:
        return self.grid[pos.row][pos.col] == CellType.OBSTACLE

    def can_move(self, direction: Direction) -> bool:
        """
        Sprawdzanie czy można się ruszyć z aktualnej pozycji w podanym kierunku:
        - nie wychodiz poza planszę
        - nie wchodzi na przeszkodę
        """
        dr, dc = self._direction_delta(direction)
        new_pos = Position(self.current.row + dr, self.current.col + dc)
        if not self.is_inside(new_pos):
            return False
        if self.is_obstacle(new_pos):
            return False
        return True

    def move(self, direction: Direction) -> bool:
        """
        wykonanie ruchu jeśli jest możliwy.
        Zwraca True, jeśli ruch się udał, False jeśli nie.
        """
        if not self.can_move(direction):
            return False
        dr, dc = self._direction_delta(direction)
        self.current = Position(self.current.row + dr, self.current.col + dc)
        return True



    def to_char(self, pos: Position) -> str:
        cell = self.grid[pos.row][pos.col]
        if pos == self.current and cell not in (CellType.START, CellType.STOP):

            return "@"
        if cell == CellType.START:
            return "A"  # START
        if cell == CellType.STOP:
            return "B"  # STOP
        if cell == CellType.OBSTACLE:
            return "X"
        return "."  # puste pole

    def to_string(self) -> str:
        """
        Zwraca tekstową reprezentację planszy
        """
        lines = []
        for r in range(self.rows):
            line_chars = [self.to_char(Position(r, c)) for c in range(self.cols)]
            lines.append(" ".join(line_chars))
        return "\n".join(lines)
