import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic_utils import check_guess

def test_winning_guess():
    # Access index [0] to get the outcome string
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    result = check_guess(40, 50)
    assert result[0] == "Too Low"