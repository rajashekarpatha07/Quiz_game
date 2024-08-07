import tkinter as tk
from tkinter import messagebox, font

quiz_questions = [
    {
        "question": "Who is known as the father of the computer?",
        "choices": ["Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs"],
        "answer": "Charles Babbage"
    },
    {
        "question": "What does CPU stand for?",
        "choices": ["Central Processing Unit", "Computer Personal Unit", "Central Power Unit", "Computer Processing Unit"],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which company developed the first commercial microprocessor?",
        "choices": ["Intel", "AMD", "IBM", "Microsoft"],
        "answer": "Intel"
    },
    {
        "question": "What year was the World Wide Web introduced to the public?",
        "choices": ["1985", "1990", "1991", "1995"],
        "answer": "1991"
    },
    {
        "question": "What programming language is primarily used for developing Android apps?",
        "choices": ["Swift", "Java", "Python", "Ruby"],
        "answer": "Java"
    },
    {
        "question": "Which social media platform was launched first?",
        "choices": ["Facebook", "Twitter", "LinkedIn", "Instagram"],
        "answer": "LinkedIn"
    },
    {
        "question": "What does RAM stand for in computing?",
        "choices": ["Random Access Memory", "Read Access Memory", "Rapid Access Memory", "Real-time Access Memory"],
        "answer": "Random Access Memory"
    },
    {
        "question": "Which company is known for creating the iPhone?",
        "choices": ["Microsoft", "Google", "Apple", "Samsung"],
        "answer": "Apple"
    },
    {
        "question": "What does HTTP stand for?",
        "choices": ["HyperText Transfer Protocol", "HyperText Transfer Platform", "HyperText Transmission Protocol", "HyperText Transmission Platform"],
        "answer": "HyperText Transfer Protocol"
    },
    {
        "question": "Which technology is used to make telephone calls over the Internet possible?",
        "choices": ["VoIP", "GSM", "LTE", "PSTN"],
        "answer": "VoIP"
    }
]

class QuizGame(tk.Tk):
    def __init__(self, questions):
        super().__init__()
        self.title("Quiz Game")
        self.geometry("600x500")
        self.configure(bg="#fafafa")
        self.questions = questions
        self.current_question = 0
        self.score = 0
        self.time_left = 30  # Timer starts at 30 seconds

        # Font styles
        self.title_font = font.Font(family='Arial', size=18, weight='bold')
        self.question_font = font.Font(family='Arial', size=14)
        self.choice_font = font.Font(family='Arial', size=12)
        self.progress_font = font.Font(family='Arial', size=12, weight='bold')
        self.timer_font = font.Font(family='Arial', size=14, weight='bold')

        # Title label
        self.title_label = tk.Label(self, text="Welcome to the Quiz Game", font=self.title_font, bg="#FFDDC1", fg="#333", padx=20, pady=10, relief=tk.RAISED, borderwidth=2)
        self.title_label.pack(pady=10)

        # Timer label
        self.timer_label = tk.Label(self, text="", font=self.timer_font, bg="#FFDDC1", fg="#333")
        self.timer_label.pack(pady=5)

        # Progress label
        self.progress_label = tk.Label(self, text="", font=self.progress_font, bg="#FFDDC1", fg="#333")
        self.progress_label.pack(pady=5)

        # Question label
        self.question_label = tk.Label(self, text="", wraplength=560, font=self.question_font, bg="#FFDDC1", fg="#333", padx=10, pady=10, relief=tk.GROOVE, borderwidth=2)
        self.question_label.pack(pady=10)

        # IntVar to track selected option
        self.selected_option = tk.IntVar()

        # Radio buttons for choices
        self.radio_buttons = []
        
        for i in range(4):
            rb = tk.Radiobutton(self, text="", variable=self.selected_option, value=i, font=self.choice_font, bg="#E0F2F1", selectcolor="#B2DFDB", activebackground="#B2DFDB", padx=10, pady=5, relief=tk.RAISED, borderwidth=1)
            rb.pack(anchor=tk.W, padx=20, pady=5)
            self.radio_buttons.append(rb)

        # Submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.check_answer, bg="#4CAF50", fg="#fff", font=self.choice_font, padx=10, pady=5, relief=tk.RAISED, borderwidth=2)
        self.submit_button.pack(pady=20)

        # Reset button
        self.reset_button = tk.Button(self, text="Restart Quiz", command=self.reset_quiz, bg="#FFC107", fg="#fff", font=self.choice_font, padx=10, pady=5, relief=tk.RAISED, borderwidth=2)
        self.reset_button.pack(pady=10)

        # Load the first question
        self.load_question()
        self.update_timer()

    def load_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question["question"])
            for i, choice in enumerate(question["choices"]):
                self.radio_buttons[i].config(text=choice, value=i)
                self.radio_buttons[i].config(bg="#E0F2F1", fg="#333")  # Reset colors
            
            # Update progress label
            self.progress_label.config(text=f"Question {self.current_question + 1} of {len(self.questions)}")
        else:
            self.end_quiz()

    def update_choice_color(self, selected_index):
        for i, rb in enumerate(self.radio_buttons):
            if i == selected_index:
                rb.config(bg="#B2DFDB", fg="#000")  # Highlight selected choice
            else:
                rb.config(bg="#E0F2F1", fg="#333")  # Default color for unselected choices

    def update_timer(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Time left: {self.time_left}s")
            self.time_left -= 1
            self.after(1000, self.update_timer)
        else:
            self.check_answer()  # Automatically submit answer if time runs out

    def check_answer(self):
        selected_index = self.selected_option.get()
        if selected_index < 0 or selected_index >= len(self.radio_buttons):
            messagebox.showwarning("No Selection", "Please select an option before submitting.")
            return
        
        selected_answer = self.radio_buttons[selected_index].cget("text")
        
        if selected_answer == self.questions[self.current_question]["answer"]:
            self.score += 1
            messagebox.showinfo("Correct", "Correct option!!! You got 1 point")
        else:
            messagebox.showinfo("Incorrect", "It's incorrect")

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.time_left = 30  # Reset timer for the next question
            self.load_question()
        else:
            self.end_quiz()

    def end_quiz(self):
        messagebox.showinfo("Quiz Completed", f"You got {self.score} points")
        self.quit()

    def reset_quiz(self):
        self.current_question = 0
        self.score = 0
        self.time_left = 30
        self.selected_option.set(-1)  # Reset selected option
        self.load_question()
        self.submit_button.config(state=tk.NORMAL)  # Re-enable submit button
        self.update_timer()

if __name__ == "__main__":
    app = QuizGame(quiz_questions)
    app.mainloop()
