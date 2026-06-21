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
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
AI suggested reseting the status back to "playing" if new game, since New game was not working before. I verified by using New game after the fix, and it works now.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
