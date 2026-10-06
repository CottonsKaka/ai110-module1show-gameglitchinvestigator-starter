# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] The game's purpose is to let the user guess a secret number and receive hints until they win.
- [x] I found that the secret number changed whenever I clicked **Submit**, and the game’s "Higher/Lower" hints were incorrect.
- [x] I fixed the game logic with help from AI by looking at the errors, asking for debugging guidance, and applying the suggested fixes. My experience was great because I learned how to debug with AI.

## Demo Walkthrough

1. User enters a guess of 40.
2. The game returns **"Too Low"** and updates the score.
3. User enters a guess of 70, and the game returns **"Too High"** while updating the score again.
4. User enters the correct guess of 55, and the game confirms the win.
5. The game ends after the correct guess, with the final score displayed.

## 🧪 Test Results

```
$ .venv/bin/python -m pytest -q tests/test_game_logic.py
.......                                                                  [100%]
7 passed in 0.65s
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
