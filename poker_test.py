
import poker
import pytest


def test_white_win():
    Black,White = "2H 3D 5S 9C KD" , "2C 3H 4S 8C AH"
    player, opponent = poker.PokerHand(Black), poker.PokerHand(White)
    assert(player.compare_with(opponent) == "White win")

def test_black_win():
    Black, White = "2H 4S 4C 2D 4H", "2S 8S AS QS 3S"
    player, opponent = poker.PokerHand(Black), poker.PokerHand(White)
    assert (player.compare_with(opponent) == "Black Win")

def test_tie():
    Black, White = "2H 3D 5S 9C KD", "2D 3H 5C 9S KH"
    player, opponent = poker.PokerHand(Black), poker.PokerHand(White)
    assert (player.compare_with(opponent) == "Black Tie")
