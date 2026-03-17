# 🎮 Tic-Tac-Toe: Python OOP Project

## 📌 About The Project
This project is a classic terminal-based Tic-Tac-Toe game written entirely in Python. 

I developed this game as a practical, hands-on application of the concepts I learned in my **Python Programming Course**. The main goal was to move beyond basic scripting and build a structured, interactive program using **Object-Oriented Programming (OOP)** principles and Clean Code practices.

## 🧠 What I Learned & Applied
Building this game helped me solidify several core software engineering concepts:
* **Object-Oriented Programming (OOP):** Structuring the game using Classes and Objects.
* **Composition:** Designing classes that contain instances of other classes (e.g., the `Game` class orchestrating `Board`, `Player`, and `Menu` objects).
* **Single Responsibility Principle (SRP):** Ensuring each class handles only its specific logical domain (The Board handles the grid, the Menu handles UI, etc.).
* **Input Validation & Error Handling:** Using `try-except` blocks and loops to handle invalid user inputs gracefully without crashing the program.
* **Dynamic UX:** Implementing screen-clearing functionality (`IPython.display.clear_output`) to provide a seamless, flicker-free experience in Jupyter Notebooks.

## 🏗️ Project Structure
The project is divided into four main classes to ensure modularity:
1. `Player`: Manages player data (Name and Symbol 'X' or 'O').
2. `Board`: Manages the 3x3 grid, updates moves, and checks for win/draw conditions.
3. `Menu`: Handles user interface prompts (Main Menu, End Game Menu).
4. `Game`: The main orchestrator that controls the game loop, player turns, and overall flow.

## 🚀 How to Run
This game is optimized to run smoothly in a **Jupyter Notebook** or **Google Colab** environment.

1. Clone the repository:
   ```bash
   git clone [https://github.com/AbdulhayYassir/Tic-Tac-Toe-Project.git](https://github.com/AbdulhayYassir/Tic-Tac-Toe-Project.git)
