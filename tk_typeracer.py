from tkinter import *
from tkinter import messagebox
from timeit import default_timer as timer
import random

root = Tk()
root.title("Typing Speed")

frame1 = Frame(root, bg="black")
frame1.pack()
begin = 0
pangrams = ["The quick brown fox jumped over the lazy dog.", "Glib jocks quiz nymph to vex dwarf.",
            "Sphinx of black quartz, judge my vow.", "How quickly daft jumping zebras vex!",
            "The five boxing wizards jump quickly."]
selecSentence = random.sample(pangrams, k=1)[0]
no_chars = len(selecSentence)


def start():
    if entry1.get() != "":
        messagebox.askretrycancel("error", "You started the test after typing ")
    else:
        begin = timer()


def end():
    global begin, no_chars

    final = entry1.get()
    if final == "":
        messagebox.showerror("Error", "The sentence has not been typed, please try again.")
    else:
        complete = timer()
        elapsed = complete - begin
        correct = 0
        wrong = 0
        for i in range(len(selecSentence)):
            if final[i] == selecSentence[i]:
                correct += 1
            else:
                wrong += 1
        accuracy = (correct / no_chars) * 100
        messagebox.showinfo("Success",
                            "Your time was " + str(elapsed) + " seconds and your accuracy was " + str(accuracy) + "%")
        root.quit()


dispLabel = Label(frame1, text=selecSentence, fg="white", bg="black")
dispLabel.grid(row=0, column=0, columnspan=4)
entry1 = Entry(frame1, width=50)
entry1.grid(row=1, column=0)
endButton = Button(frame1, text="End", fg="white", bg="black", command=end)
endButton.grid(row=3, column=0, sticky="news")
startButton = Button(frame1, text="Start", fg="white", bg="black", command=start)
startButton.grid(row=2, column=0, sticky="news")

root.mainloop()
