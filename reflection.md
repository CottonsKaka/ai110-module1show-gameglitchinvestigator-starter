# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, it looked like a normal number-guessing game, but several parts did not work correctly. The game displayed the wrong number of attempts remaining because the attempt counter started at 1 instead of 0. The hints were also backwards: when my guess was higher than the secret number, the game told me to guess higher instead of lower. After the game reaches the game-over screen, clicking the button to start over should refresh the game immediately, but I had to refresh the whole page before the new state appeared.

### Bug Reproduction Logs

| Input or Trigger | Expected Behavior | Actual Behavior | Code Cause or Suspicious Location |
|---|---|---|---|
| Start a game with a 5-attempt limit and submit guesses | The player should receive all 5 allowed guesses, and the attempts-left display should be accurate. | The game starts with 1 attempt already counted, so the display is off by one and a guess is effectively lost. | `st.session_state.attempts = 1` in `app.py`, around line 95. |
| Secret number is 50; enter `60` | The game should report that the guess is too high and tell me to go lower. | The game reports “Go HIGHER,” which is the opposite hint. | The `check_guess()` function in `app.py`, around lines 32–38. |
| Reach the game-over screen and click the button to start a new game | The game should reset and refresh immediately. | The game does not visibly refresh until the whole page is manually refreshed. | The game reset and rerun behavior around the `New Game 🔁` button in `app.py`. |
| Enter `abc` or submit an empty guess | The game should show an input error without using an attempt. | The attempt counter increases before the input is validated. | `st.session_state.attempts += 1` occurs before `parse_guess()` in `app.py`, around line 148. |

---

## 2. How did you use AI as a teammate?

I used Copilot in VS Code as an AI teammate. One correct suggestion was to initialize `st.session_state.attempts` to `0` instead of `1` and increment it only after `parse_guess()` confirms that the input is valid. This was correct because a new game has no guesses yet, and invalid input should not use an attempt; I verified it with Streamlit `AppTest` tests for the initial count and invalid guesses. Another suggestion was to move the “Guess a number...” message lower in the file so it would be rendered after the guess was processed. I did not accept that suggestion as written because it changed the location of the message in the interface; instead, I used a Streamlit placeholder (`st.empty()`) in the original location and updated that placeholder after processing, which fixed the count without changing the layout.

---

## 3. Debugging and testing your fixes

I verified the repairs with the Streamlit `AppTest` harness by running `./.venv/bin/python -m pytest -q tests/test_game_logic.py`; all seven tests passed. The tests confirm that guesses are classified with the correct higher/lower hint, the secret stays the same after a guess, invalid input does not consume an attempt, and the final valid guess displays `Attempts left: 0`. They also confirm that clicking New Game immediately resets the game-over state, score, history, attempt count, and input field. AI helped me turn each observed bug into a focused regression test, and I reviewed the results to make sure the fix preserved the original layout.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
