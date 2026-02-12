PIECES = "PBRQK"
KING = 'K'
PAWN = 'P'
ROOK = 'R'
BISHOP = 'B'
QUEEN = 'Q'

# Direction vectors: (row_delta, col_delta)
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
UP_LEFT = (-1, -1)
UP_RIGHT = (-1, 1)
DOWN_LEFT = (1, -1)
DOWN_RIGHT = (1, 1)

STRAIGHT_DIRS = [UP, DOWN, LEFT, RIGHT]
DIAGONAL_DIRS = [UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT]
QUEEN_DIRS = STRAIGHT_DIRS + DIAGONAL_DIRS

# Map sliding pieces to their allowed directions
PIECE_DIRECTIONS = {
    ROOK: STRAIGHT_DIRS,
    BISHOP: DIAGONAL_DIRS,
    QUEEN: QUEEN_DIRS,
}

PAWN_ATTACKS = [UP_LEFT, UP_RIGHT]  # pawns attack diagonally upwards


def checkmate(board):
    """Check if the lone King on the board is in check.

    board: multiline string where each line is a board row.
    Prints "Success" if King is in check, otherwise prints "Fail".
    """
    rows = board.strip().split('\n')
    size = len(rows)

    # basic validation: non-empty square board
    if size == 0:
        return
    for row in rows:
        if len(row) != size:
            return

    # find the king; there must be exactly one
    king_pos = None
    for row in range(size):
        for col in range(size):
            if rows[row][col] == KING:
                if king_pos is not None:
                    return
                king_pos = (row, col)
    if king_pos is None:
        return

    # scan every square; if any piece can attack the king -> Success
    for row in range(size):
        for col in range(size):
            piece = rows[row][col]
            if piece == PAWN:
                if pawn_can_attack(row, col, king_pos):
                    print("Success")
                    return
            elif piece in PIECE_DIRECTIONS:
                if sliding_piece_can_attack(rows, row, col, piece, king_pos):
                    print("Success")
                    return

    print("Fail")


def pawn_can_attack(pawn_row, pawn_col, king_pos):
    king_row, king_col = king_pos
    # pawns attack one row up and one column left/right
    return (king_row == pawn_row - 1) and (abs(king_col - pawn_col) == 1)


def sliding_piece_can_attack(rows, piece_row, piece_col, piece, king_pos):
    """Generic check for Rook/Bishop/Queen using piece direction lists."""
    king_row, king_col = king_pos
    allowed_dirs = PIECE_DIRECTIONS[piece]
    for dir_row, dir_col in allowed_dirs:
        if check_line_for_king(rows, piece_row, piece_col, dir_row, dir_col, king_row, king_col):
            return True
    return False


def check_line_for_king(rows, start_row, start_col, step_row, step_col, king_row, king_col):
    """Step along (step_row, step_col) from (start_row,start_col).
    If we encounter the king first -> True. If any other piece blocks -> False.
    """
    size = len(rows)
    r = start_row + step_row
    c = start_col + step_col
    while 0 <= r < size and 0 <= c < size:
        if (r, c) == (king_row, king_col):
            return True
        if rows[r][c] in PIECES:
            return False
        r += step_row
        c += step_col
    return False


def visualize_board(board):
    """Print a simple, human-readable view of the board.

    Example output for a 4x4 board:
      cols: 0 1 2 3
    row 0: R . . .
    row 1: . K . .
    ...
    """
    rows = board.strip().split('\n')
    visualize_rows(rows)


def visualize_rows(rows):
    """Print rows (list of strings) with coordinates and '.' for empty.
    This is separate from `visualize_board` so callers that already have parsed
    rows can reuse it.
    """
    size = len(rows)
    if size == 0:
        print("(empty board)")
        return

    # Header with column indices
    cols = ' '.join(str(c) for c in range(size))
    print(f"cols: {cols}")

    # Each row: show index then pieces or '.'
    for r, row in enumerate(rows):
        cells = []
        for ch in row:
            cells.append(ch if ch in PIECES else '.')
        print(f"row {r}: " + ' '.join(cells))


__all__ = [
    'checkmate',
    'visualize_board',
    'visualize_rows',
]
