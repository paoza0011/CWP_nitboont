def checkmate(board):
    if not isinstance(board, str):
        return

    rows = board.splitlines()

    if not rows:
        return

    size = len(rows)

    # เช็กว่ากระดานเป็นสี่เหลี่ยมจัตุรัส
    for row in rows:
        if len(row) != size:
            return

    # หา King
    kings = []

    for row in range(size):
        for col in range(size):
            if rows[row][col] == "K":
                kings.append((row, col))

    # ต้องมี King 1 ตัว
    if len(kings) != 1:
        return

    king_row, king_col = kings[0]

    # -------------------------
    # Pawn
    # -------------------------
    pawn_rows = [king_row - 1, king_row + 1]

    for pawn_row in pawn_rows:
        if 0 <= pawn_row < size:

            # ซ้าย
            if king_col - 1 >= 0:
                if rows[pawn_row][king_col - 1] == "P":
                    print("Success")
                    return

            # ขวา
            if king_col + 1 < size:
                if rows[pawn_row][king_col + 1] == "P":
                    print("Success")
                    return

    # -------------------------
    # Rook and Queen
    # เดินตรง
    # -------------------------
    straight = [
        (-1, 0),   # ขึ้น
        (1, 0),    # ลง
        (0, -1),   # ซ้าย
        (0, 1),    # ขวา
    ]

    for dr, dc in straight:
        row = king_row + dr
        col = king_col + dc

        while 0 <= row < size and 0 <= col < size:
            piece = rows[row][col]

            if piece in "PBRQK":
                if piece == "R" or piece == "Q":
                    print("Success")
                    return

                break

            row += dr
            col += dc

    # -------------------------
    # Bishop and Queen
    # เดินเฉียง
    # -------------------------
    diagonal = [
        (-1, -1),  # บนซ้าย
        (-1, 1),   # บนขวา
        (1, -1),   # ล่างซ้าย
        (1, 1),    # ล่างขวา
    ]

    for dr, dc in diagonal:
        row = king_row + dr
        col = king_col + dc

        while 0 <= row < size and 0 <= col < size:
            piece = rows[row][col]

            if piece in "PBRQK":
                if piece == "B" or piece == "Q":
                    print("Success")
                    return

                break

            row += dr
            col += dc

    print("Fail")