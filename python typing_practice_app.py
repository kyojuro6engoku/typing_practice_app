import tkinter as tk
import random
import time

# List of words for typing practice
words = ['python', 'programming', 'practice', 'keyboard', 'challenge', 'developer', 'coding', 'algorithm', 'exercise']

def start_typing():
    global current_word, start_time
    current_word = random.choice(words)
    word_label.config(text=current_word)
    start_time = time.time()
    input_entry.delete(0, tk.END)
    input_entry.focus()

def check_typing(event):
    global current_word, start_time
    typed_word = input_entry.get().strip()
    if typed_word == current_word:
        elapsed_time = time.time() - start_time
        wpm = int(len(current_word) / (elapsed_time / 60) / 5)  # Assuming an average word length of 5 characters
        result_label.config(text=f"Correct! Your WPM: {wpm}")
    else:
        result_label.config(text="Incorrect! Try again.")
    input_entry.delete(0, tk.END)

# Create the main application window
app = tk.Tk()
app.title("Typing Practice App")
app.geometry("400x200")

# UI Components
word_label = tk.Label(app, text="", font=("Helvetica", 24))
word_label.pack(pady=20)

input_entry = tk.Entry(app, font=("Helvetica", 16))
input_entry.pack(pady=10)
input_entry.bind("<Return>", check_typing)

start_button = tk.Button(app, text="Start Typing", font=("Helvetica", 16), command=start_typing)
start_button.pack(pady=10)

result_label = tk.Label(app, text="", font=("Helvetica", 16))
result_label.pack(pady=20)

app.mainloop()
