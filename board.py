from piece import Piece


def build_pieces(board_size):
    """Builds the starting game pieces"""
    assert board_size == 8
    letters = ["R", "N", "B", "Q", "K", "B", "N", "R"]
    output = []
    for i in range(1, board_size + 1):
        output.append(Piece("W", letters[i - 1], i, 1))
    for i in range(1, board_size + 1):
        output.append(Piece("W", "P", i, 2))
    for i in range(1, board_size + 1):
        output.append(Piece("B", "P", i, board_size - 1))
    for i in range(1, board_size + 1):
        output.append(Piece("B", letters[i - 1], i, board_size))
    return output


def search_by_indexes(pieces, i, j):
    """Searches for the piece at the given coordinates"""
    for piece in pieces:
        if (piece.i() == i) and (piece.j() == j):
            return piece
    return None
