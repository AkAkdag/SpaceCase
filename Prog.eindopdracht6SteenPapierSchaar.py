import tkinter as tk
import random

# Define the window
window = tk.Tk()
window.title("🪨 📄 ✂️")
window.geometry("300x200")

# Define the game logic
choices = ["🪨", "📄", "✂️"]
def play(choice):
    computer_choice = random.choice(choices)
    if choice == computer_choice:
        result_label.config(text="Het is gelijkspel!")
    elif (choice == "🪨" and computer_choice == "✂️") or \
         (choice == "📄" and computer_choice == "🪨") or \
         (choice == "✂️" and computer_choice == "📄"):
        result_label.config(text="Jij wint!")
    else:
        result_label.config(text="Jij verliest!")

# Define the UI elements
title_label = tk.Label(text="🪨 📄 ✂️", font=("Arial", 14))
title_label.pack()

rock_button = tk.Button(text="🪨", font=("Arial", 14), command=lambda: play("🪨"))
rock_button.pack()

paper_button = tk.Button(text="📄", font=("Arial", 14), command=lambda: play("📄"))
paper_button.pack()

scissors_button = tk.Button(text="✂️", font=("Arial", 14), command=lambda: play("✂️"))
scissors_button.pack()

result_label = tk.Label(text="")
result_label.pack()

# Start the main loop
window.mainloop()
