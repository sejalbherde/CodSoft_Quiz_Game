import random
import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("600x400")
        self.root.configure(bg="pink")  # Set background color to blue

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "Madrid", "Rome", "Berlin"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which city is the capital of Australia?",
                "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
                "correct_answer": "Canberra"
            },
            {
                "question": "What is the capital of Brazil?",
                "options": ["Rio de Janeiro", "Brasília", "São Paulo", "Salvador"],
                "correct_answer": "Brasília"
            },
            {
                "question": "What is the capital of India?",
                "options": ["Delhi", "Mumbai", "Pune", "Nagpur"],
                "correct_answer": "Delhi"
            }
        ]

        self.score = 0
        self.current_question = 0

        self.question_label = tk.Label(root, text="", font=("Helvetica", 16), wraplength=500, bg="#007BFF", fg="white")
        self.question_label.pack(pady=20)

        self.option_var = tk.StringVar()
        self.option_frame = tk.Frame(root, bg="#007BFF")  # Frame for options
        self.option_frame.pack()

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.option_frame, text="", font=("Helvetica", 12), width=20, bg="#4CAF50", fg="white",
                               command=lambda i=i: self.check_answer(self.questions[self.current_question]["options"][i]))
            button.grid(row=i, column=0, padx=10, pady=5)
            self.option_buttons.append(button)

        self.next_button = tk.Button(root, text="Next Question", command=self.next_question, bg="#007BFF", fg="white", state=tk.DISABLED)
        self.next_button.pack()

        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            self.question_label.config(text=q["question"])

            if "options" in q:
                for i in range(4):
                    self.option_buttons[i].config(text=q["options"][i], state=tk.NORMAL)
                self.next_button.config(state=tk.DISABLED)
            else:
                for button in self.option_buttons:
                    button.config(state=tk.DISABLED)
                self.next_button.config(state=tk.NORMAL)
        else:
            self.show_final_score()

    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question]["correct_answer"]

        if selected_option.lower() == correct_answer.lower():
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"Sorry, the correct answer is: {correct_answer}")

        self.current_question += 1
        self.load_question()

    def next_question(self):
        self.load_question()

    def show_final_score(self):
        messagebox.showinfo("Quiz Completed", f"Your final score is: {self.score}/{len(self.questions)}")
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
