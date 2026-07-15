# 🎯 Number Guessing Game

A simple command-line Number Guessing Game built with Python. The program randomly generates a number between **1 and 100**, and the player must guess it. After each guess, the game provides feedback indicating whether the guess is too high or too low until the correct number is found.

---

## 📌 Features

- 🎲 Random number generation
- 🔢 User input validation
- 📈 Hints if the guess is too high or too low
- 🏆 Counts the number of attempts
- ❌ Handles invalid (non-numeric) input gracefully
- 🖥️ Easy-to-use command-line interface

---

## 🛠️ Technologies Used

- Python 3
- Built-in `random` module

---

## 📂 Project Structure

```
number-guessing-game/
│
├── number_guessing_game.py
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/number-guessing-game.git
```

### 2. Navigate to the project folder

```bash
cd number-guessing-game
```

### 3. Run the program

```bash
python number_guessing_game.py
```

---

## 🎮 How to Play

1. Run the program.
2. The computer randomly selects a number between **1 and 100**.
3. Enter your guess.
4. The game will tell you if your guess is:
   - 📉 Too Low
   - 📈 Too High
5. Keep guessing until you find the correct number.
6. The game displays the total number of attempts when you win.

---

## 💻 Example Output

```text
🎯 Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Enter your guess: 50
📈 Too high! Try again.

Enter your guess: 20
📉 Too low! Try again.

Enter your guess: 35

🎉 Congratulations!
You guessed the number 35.
You took 3 attempt(s).
```

---

## 🧠 Concepts Used

- Variables
- Loops (`while`)
- Conditional Statements (`if`, `elif`, `else`)
- Functions from the `random` module
- Exception Handling (`try` / `except`)
- User Input
- Basic Python Programming

---

## 🚀 Future Improvements

- 🎯 Difficulty Levels (Easy, Medium, Hard)
- ❤️ Limited Attempts
- 🔄 Play Again Option
- 💾 High Score Tracking
- 💡 Hint System
- 📊 Scoreboard
- 🖥️ GUI Version using Tkinter or PyQt

---

## 🎓 Learning Outcomes

This project helps beginners practice:

- Python syntax
- Problem-solving
- Control flow
- Error handling
- Working with random numbers
- Building interactive command-line applications

---

