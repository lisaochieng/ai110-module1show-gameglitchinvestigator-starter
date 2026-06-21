# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  It looked normal, the ux was decent game instructions are clear.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  my input was 40, kept telling me to go higher even though the answer was 2, lower
  I have one attempt left but it says I have 0 left
  After a game, the new game button doesn't work
  my input was 77, expected is 78, it tells me to go lower instead
  history logs are one step behind

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|49 |go lower (40) |go higher |it should tell me to go lower |
|new game |be able to start a new game  |unable to submit guesses |new game button does not work |
|3 |go higher (73) |go lower | it should tell me to go higher|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Claude, Copilot, and Gemini.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  The AI suggested resetting the status back to "playing" if the new game button was clicked, since the button was not working before. I verified by running the app, clicking 'New Game' after a finished round, and confirming I could submit guesses again.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  The AI correctly suggested fixing a logic bug by casting inputs to integers, but it gave me the wrong text for the hints, telling me to return "Go HIGHER!" when my guess was greater than the secret. I verified this was misleading by playing the live game, entering a massive number, and watching the game tell me to keep going higher. I had to go into `logic_utils.py` and manually swap the strings so the logic actually made sense for the player.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I decided a bug was truly fixed only after verifying it in both my automated tests and the live Streamlit app. For example, when I fixed the reversed hint logic, I first made sure the `pytest` assertions passed for both the "Too High" and "Too Low" scenarios. Afterward, I ran the app, manually entered a deliberate wrong guess, and visually confirmed that the game gave me the correct direction. 
  
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I wrote and ran a `pytest` case named `test_guess_too_high` which passed a guess of 60 and a secret of 50 into the `check_guess` function. When I first ran the test, it failed because the function returns a tuple (the status and the UI message), but my test was looking for a single string. This showed me exactly how my data was formatted and taught me to use `result[0]` in my assertions to specifically check the outcome string.

- Did AI help you design or understand any tests? How?
  Yes, the AI was highly involved in helping me understand the test failures. Aside from explaining the tuple issue mentioned above, it also helped me resolve a tricky `ModuleNotFoundError` when `pytest` couldn't locate my refactored logic. It showed me how to use `sys.path.append` and `__init__.py` files so my test directory could successfully import `logic_utils.py`.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit basically reruns your whole Python script from top to bottom every time you click a button or interact with the app. Session state is just a built-in dictionary where you can save variables (like the score or the secret number) so they don't get wiped out every time the page reloads.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  I want to keep separating my core game logic from my UI code into files like `logic_utils.py`. It made writing `pytest` cases way easier because I didn't have to deal with Streamlit's interface code.
  
- What is one thing you would do differently next time you work with AI on a coding task?
  I won't just assume the code is correct just because it doesn't throw an error. I need to actually playtest the game right away to make sure the underlying logic makes sense.
  
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  I used to think AI code was mostly ready to copy-paste, but now I treat it like a rough draft. It gets the structure down, but you still have to go in and fix the logical blind spots yourself.

