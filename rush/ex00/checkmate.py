def checkmate(board):
    try:
        rows = board.strip().split('\n')
        n = len(rows)
        if n == 0:
            return
        for row in rows:
            if len(row) != n:
                return

        # หา King (ต้องมีแค่ตัวเดียว)
        king = None
        for r in range(n):
            for c in range(n):
                if rows[r][c] == 'K':
                    if king:
                        return
                    king = (r, c)
        if not king:
            return

        # เช็คทุกตัวหมากว่าจับ King ได้ไหม
        for r in range(n):
            for c in range(n):
                if can_attack(rows[r][c], r, c, king, rows):
                    print("Success")
                    return
        print("Fail")
    except Exception:
        return


def can_attack(piece, r, c, king, rows):
    kr, kc = king
    dr = kr - r
    dc = kc - c

    # Pawn: จับทแยงขึ้น 1 ช่อง
    if piece == 'P':
        return dr == -1 and abs(dc) == 1

    # ทิศที่แต่ละตัวเดินได้
    # R = ตรง, B = ทแยง, Q = ตรง+ทแยง
    dirs = {
        'R': dr == 0 or dc == 0,
        'B': abs(dr) == abs(dc),
        'Q': dr == 0 or dc == 0 or abs(dr) == abs(dc),
    }
    if piece not in dirs or not dirs[piece] or (dr == 0 and dc == 0):
        return False

    # หาทิศทาง แล้วเดินเช็คว่ามีตัวขวางไหม
    sr = (1 if dr > 0 else -1) if dr != 0 else 0
    sc = (1 if dc > 0 else -1) if dc != 0 else 0
    r, c = r + sr, c + sc
    while (r, c) != (kr, kc):
        if rows[r][c] in "PBRQK":
            return False
        r += sr
        c += sc
    return True