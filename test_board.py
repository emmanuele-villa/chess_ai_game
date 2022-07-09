from board import build_pieces, search_by_indexes
from piece import Piece


def test_build_pieces():
    """Tests the board pieces creation"""
    pieces = build_pieces(8)
    assert pieces[0] == Piece("B", "T", 0, 0)
    assert pieces[1] == Piece("B", "N", 0, 1)
    assert pieces[2] == Piece("B", "B", 0, 2)
    assert pieces[3] == Piece("B", "K", 0, 3)
    assert pieces[4] == Piece("B", "Q", 0, 4)
    assert pieces[5] == Piece("B", "B", 0, 5)
    assert pieces[6] == Piece("B", "N", 0, 6)
    assert pieces[7] == Piece("B", "T", 0, 7)
    assert pieces[8] == Piece("B", "P", 1, 0)
    assert pieces[9] == Piece("B", "P", 1, 1)
    assert pieces[10] == Piece("B", "P", 1, 2)
    assert pieces[11] == Piece("B", "P", 1, 3)
    assert pieces[12] == Piece("B", "P", 1, 4)
    assert pieces[13] == Piece("B", "P", 1, 5)
    assert pieces[14] == Piece("B", "P", 1, 6)
    assert pieces[15] == Piece("B", "P", 1, 7)
    assert pieces[16] == Piece("W", "P", 6, 0)
    assert pieces[17] == Piece("W", "P", 6, 1)
    assert pieces[18] == Piece("W", "P", 6, 2)
    assert pieces[19] == Piece("W", "P", 6, 3)
    assert pieces[20] == Piece("W", "P", 6, 4)
    assert pieces[21] == Piece("W", "P", 6, 5)
    assert pieces[22] == Piece("W", "P", 6, 6)
    assert pieces[23] == Piece("W", "P", 6, 7)
    assert pieces[24] == Piece("W", "T", 7, 0)
    assert pieces[25] == Piece("W", "N", 7, 1)
    assert pieces[26] == Piece("W", "B", 7, 2)
    assert pieces[27] == Piece("W", "K", 7, 3)
    assert pieces[28] == Piece("W", "Q", 7, 4)
    assert pieces[29] == Piece("W", "B", 7, 5)
    assert pieces[30] == Piece("W", "N", 7, 6)
    assert pieces[31] == Piece("W", "T", 7, 7)


def test_search_by_indexes_match():
    """Tests the search by indexes finding something"""
    pieces = [Piece("", "", 0, 0)]
    assert search_by_indexes(pieces, 0, 0) == pieces[0]


def test_search_by_indexes_empty_pieces():
    """Tests the search by indexes finding nothing because array is empty"""
    pieces = []
    assert search_by_indexes(pieces, 0, 0) is None


def test_search_by_indexes_not_match():
    """Tests the search by indexes finding nothing because no matches are present"""
    pieces = [Piece("", "", 0, 0)]
    assert search_by_indexes(pieces, 0, 1) is None
