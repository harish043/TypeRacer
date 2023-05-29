import tkinter as tk
from tkinter import messagebox
from timeit import default_timer as timer
import random

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed")

        self.frame1 = tk.Frame(self.root, bg="black")
        self.frame1.pack()
        self.start_time = 0
        self.pangrams = [
            "The quick brown fox jumped over the lazy dog.",
            "Glib jocks quiz nymph to vex dwarf.",
            "Sphinx of black quartz, judge my vow.",
            "How quickly daft jumping zebras vex!",
            "The five boxing wizards jump quickly."
        ]
        self.selected_sentence = random.choice(self.pangrams)
        self.no_chars = len(self.selected_sentence)

        self.dispLabel = tk.Label(self.frame1, text=self.selected_sentence, fg="white", bg="black")
        self.dispLabel.grid(row=0, column=0, columnspan=4)

        self.entry1 = tk.Entry(self.frame1, width=50)
        self.entry1.grid(row=1, column=0)

        self.endButton = tk.Button(self.frame1, text="End", fg="white", bg="black", command=self.end)
        self.endButton.grid(row=3, column=0, sticky="news")

        self.startButton = tk.Button(self.frame1, text="Start", fg="white", bg="black", command=self.start)
        self.startButton.grid(row=2, column=0, sticky="news")

    def start(self):
        if self.entry1.get() != "":
            messagebox.askretrycancel("Error", "You started the test after typing")
        else:
            self.start_time = timer()

    def end(self):
        final = self.entry1.get()
        if final == "":
            messagebox.showerror("Error", "The sentence has not been typed, please try again.")
        else:
            complete = timer()
            elapsed = complete - self.start_time
            correct = sum(final[i] == self.selected_sentence[i] for i in range(len(self.selected_sentence)))
            accuracy = (correct / self.no_chars) * 100
            messagebox.showinfo(
                "Success",
                f"Your time was {elapsed:.2f} seconds and your accuracy was {accuracy:.2f}%"
            )
            self.root.quit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    app.run()
