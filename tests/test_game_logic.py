from logic_utils import check_guess
from streamlit.testing.v1 import AppTest

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")


def test_invalid_guess_does_not_consume_attempt():
    app = AppTest.from_file("app.py").run()

    app.text_input(key="guess_input_Normal").set_value("not a number")
    app.button[0].click().run()

    assert app.session_state["attempts"] == 0


def test_secret_stays_the_same_after_a_guess():
    app = AppTest.from_file("app.py").run()
    secret_before_guess = app.session_state["secret"]

    app.text_input(key="guess_input_Normal").set_value("0")
    app.button[0].click().run()

    assert app.session_state["secret"] == secret_before_guess


def test_new_game_resets_game_over_state_and_guess_input():
    app = AppTest.from_file("app.py").run()

    for _ in range(8):
        app.text_input(key="guess_input_Normal").set_value("0")
        app.button[0].click().run()

    assert app.session_state["status"] == "lost"
    assert app.session_state["attempts"] == 8

    app.button[1].click().run()

    assert app.session_state["status"] == "playing"
    assert app.session_state["attempts"] == 0
    assert app.session_state["score"] == 0
    assert app.session_state["history"] == []
    assert app.text_input(key="guess_input_Normal").value == ""


def test_final_guess_shows_zero_attempts_left():
    app = AppTest.from_file("app.py").run()

    for _ in range(8):
        app.text_input(key="guess_input_Normal").set_value("0")
        app.button[0].click().run()

    assert app.info[0].value == "Guess a number between 1 and 100. Attempts left: 0"
