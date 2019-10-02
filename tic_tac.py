# tic tac toe


from tkinter import *
from tkinter import messagebox

c = 1


def reset_play_screen():
    global c, b1, b2, b3, b4, b5, b6, b7, b8, b9
    c = 1

    b1 = Button(root, text="", width=10, height=5, command=lambda: click(b1))
    b1.grid(row=0, column=0)

    b2 = Button(root, text="", width=10, height=5, command=lambda: click(b2))
    b2.grid(row=0, column=1)

    b3 = Button(root, text="", width=10, height=5, command=lambda: click(b3))
    b3.grid(row=0, column=2)

    b4 = Button(root, text="", width=10, height=5, command=lambda: click(b4))
    b4.grid(row=1, column=0)

    b5 = Button(root, text="", width=10, height=5, command=lambda: click(b5))
    b5.grid(row=1, column=1)

    b6 = Button(root, text="", width=10, height=5, command=lambda: click(b6))
    b6.grid(row=1, column=2)

    b7 = Button(root, text="", width=10, height=5, command=lambda: click(b7))
    b7.grid(row=2, column=0)

    b8 = Button(root, text="", width=10, height=5, command=lambda: click(b8))
    b8.grid(row=2, column=1)

    b9 = Button(root, text="", width=10, height=5, command=lambda: click(b9))
    b9.grid(row=2, column=2)


def click(b):
    global c
    c = c + 1
    if (c % 2 == 0):
        if (b["text"] == ""):
            b["text"] = "0"
            b["bg"] = "yellow"
    else:
        if (b["text"] == ""):
            b["text"] = "X"
            b["bg"] = "pink"

    if (b1["text"] == "0" and b2["text"] == "0" and b3["text"] == "0"):
        messagebox.showinfo("winner", "player 1 is winner")
        reset_play_screen()

    elif (b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X"):
        messagebox.showinfo("winner", "player 2 is winner")
        reset_play_screen()

    elif (b4["text"] == "0" and b5["text"] == "0" and b6["text"] == "0"):
        messagebox.showinfo("winner", "player 1 is winner")
        reset_play_screen()

    elif (b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X"):
        messagebox.showinfo("winner", "player 2 is winner")
        reset_play_screen()

    elif (b7["text"] == "0" and b8["text"] == "0" and b9["text"] == "0"):
        messagebox.showinfo("winner", "player 1 is winner")
        reset_play_screen()

    elif (b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X"):
        messagebox.showinfo("winner", "player 2 is winner")
        reset_play_screen()

    elif (b1["text"] == "0" and b4["text"] == "0" and b7["text"] == "0"):
        messagebox.showinfo("winner", "player 1 is winner")
        reset_play_screen()

    elif (b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X"):
        messagebox.showinfo("winner", "player 2 is winner")
        reset_play_screen()

    elif (b2["text"] == "0" and b5["text"] == "0" and b8["text"] == "0"):
        messagebox.showinfo("winner", "player 1 is winner")
        reset_play_screen()

    elif (b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X"):
        messagebox.showinfo("winner", "player 2 is winner")
        reset_play_screen()

    elif (b3["text"] == "0" and b6["text"] == "0" and b9["text"] == "0"):
        messagebox.showinfo("winner", "player 1 is winner")
        reset_play_screen()

    elif (b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X"):
        messagebox.showinfo("winner", "player 2 is winner")
        reset_play_screen()

    elif (b1["text"] == "0" and b5["text"] == "0" and b9["text"] == "0"):
        messagebox.showinfo("winner", "player 1 is winner")
        reset_play_screen()

    elif (b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X"):
        messagebox.showinfo("winner", "player 2 is winner")
        reset_play_screen()

    elif (b3["text"] == "0" and b5["text"] == "0" and b7["text"] == "0"):
        messagebox.showinfo("winner", "player 1 is winner")
        reset_play_screen()

    elif (b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X"):
        messagebox.showinfo("winner", "player 2 is winner")
        reset_play_screen()

     

root = Tk()
# root.minsize(300,300)
root.resizable(0, 0)

b1 = Button(root, text="", width=10, height=5, command=lambda: click(b1))
b1.grid(row=0, column=0)

b2 = Button(root, text="", width=10, height=5, command=lambda: click(b2))
b2.grid(row=0, column=1)

b3 = Button(root, text="", width=10, height=5, command=lambda: click(b3))
b3.grid(row=0, column=2)

b4 = Button(root, text="", width=10, height=5, command=lambda: click(b4))
b4.grid(row=1, column=0)

b5 = Button(root, text="", width=10, height=5, command=lambda: click(b5))
b5.grid(row=1, column=1)

b6 = Button(root, text="", width=10, height=5, command=lambda: click(b6))
b6.grid(row=1, column=2)

b7 = Button(root, text="", width=10, height=5, command=lambda: click(b7))
b7.grid(row=2, column=0)

b8 = Button(root, text="", width=10, height=5, command=lambda: click(b8))
b8.grid(row=2, column=1)

b9 = Button(root, text="", width=10, height=5, command=lambda: click(b9))
b9.grid(row=2, column=2)

root.title("Tic Tac Toe game")
root.config(bg="cyan")
root.mainloop()
