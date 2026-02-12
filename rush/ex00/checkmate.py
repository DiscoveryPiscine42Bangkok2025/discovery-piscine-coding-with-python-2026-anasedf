# กำหนดตัวแปร
PIECES = "PBRQK"
KING = 'K'
PAWN = 'P'
ROOK = 'R'
BISHOP = 'B'
QUEEN = 'Q'

# กำหนดทิศทาง
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
UP_LEFT = (-1, -1)
UP_RIGHT = (1, -1)
DOWN_LEFT = (-1, 1)
DOWN_RIGHT = (1, 1)

STRAIGHT_DIRS = [UP, DOWN, LEFT, RIGHT]
DIAGONAL_DIRS = [UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT]
QUEEN_DIRS = STRAIGHT_DIRS + DIAGONAL_DIRS

# เช็คกรอบ
def in_bounds(x, y, size):
    return 0 <= x < size and 0 <= y < size

# เช็คว่าหาหมากเจอทิศไหน
def is_attacked_in_direction(rows, king_x, king_y, dx, dy, size):
    x, y = king_x + dx, king_y + dy
    while in_bounds(x, y, size):
        ch = rows[y][x]
        if ch in PIECES:
            if (dx, dy) in STRAIGHT_DIRS and ch in (ROOK, QUEEN):
                return True
            if (dx, dy) in DIAGONAL_DIRS and ch in (BISHOP, QUEEN):
                return True
            return False
        x += dx
        y += dy
    return False


def checkmate(board):

    rows = board.strip().split('\n')
    size = len(rows)

    # เช็คขนาด
    if size == 0:
        return
    # เช็คขนาด
    for r in rows:
        if len(r) != size:
            return

    # เช็คจำนวนคิง
    total_kings = sum(r.count(KING) for r in rows)
    if total_kings != 1:
        return

    # หาตำแหน่งคิง
    king_pos = None
    for y, r in enumerate(rows):
        x = r.find(KING)
        if x != -1:
            king_pos = (x, y)
            break
    if king_pos is None:
        return

    king_x, king_y = king_pos

    # เช็คเบี้ย
    for dx in (-1, 1):
        px, py = king_x + dx, king_y + 1
        if in_bounds(px, py, size) and rows[py][px] == PAWN:
            print("Success")
            return

    # เช็คตัวอื่น
    for dx, dy in QUEEN_DIRS:
        if is_attacked_in_direction(rows, king_x, king_y, dx, dy, size):
            print("Success")
            return

    print("Fail")