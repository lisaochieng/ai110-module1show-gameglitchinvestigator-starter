# logic_utils.py
# FIX: Refactored core game logic into this separate file using AI assistant to separate it from UI code.

def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100

def parse_guess(raw: str):
    if not raw:
        return False, None, "Enter a guess."
    try:
        value = int(float(raw))
        return True, value, None
    except ValueError:
        return False, None, "That is not a number."

def check_guess(guess: int, secret: int):
    # FIX: Collaborated with AI to cast both inputs to int, fixing the string comparison glitch.
    guess = int(guess)
    secret = int(secret)
    
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        # FIX: Used AI to correct reversed hints; now correctly tells the player to go LOWER if guess is too high.
        return "Too High", "📉 Go LOWER!"
    
    # FIX: Corresponding hint swap so a low guess tells the user to go HIGHER.
    return "Too Low", "📈 Go HIGHER!"

def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = max(10, 100 - 10 * attempt_number)
        return current_score + points
    if outcome == "Too High":
        return current_score + 5 if attempt_number % 2 == 0 else current_score - 5
    if outcome == "Too Low":
        return current_score - 5
    return current_score