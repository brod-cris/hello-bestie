import tkinter as tk

root = tk.Tk()


def add():
    result = eval(a_text.get()) + eval(b_text.get())

    lbl_ans.configure(
        text=f'Answer : {a_text.get()} + {b_text.get()} = {result}')
# Answer = 5+5 = 10


def clear_data():
    a_text.delete(first=0, last=100)
    b_text.delete(first=0, last=100)
    a_text.focus()
    lbl_ans.configure(text="")


canvas = tk.Canvas(root, height=600, width=400, bg="#263d42")
canvas.pack()

#frame : Frame()

frame = tk.Frame(root, bg="#3e646c")
frame.place(relwidth=0.8, relheight=0.8, rely=0.1, relx=0.1)

#Text : Label()
lbl_heading = tk.Label(
    frame, text="Addition of two numbers", bg="#3e646c", fg="white")
lbl_heading.place(x=80, y=20)

# Label a : Enter the value of a:
lbl_a = tk.Label(frame, text="Enter the value of a:", bg="#3e646c", fg="white")
lbl_a.place(x=20, y=80)

# Label a : Enter the value of b:
lbl_b = tk.Label(frame, text="Enter the value of b:", bg="#3e646c", fg="white")
lbl_b.place(x=20, y=120)

#textbox : Entry()
a_text = tk.Entry(frame, width=20, bd=1)
a_text.place(x=170, y=80)

#textbox : Entry()
b_text = tk.Entry(frame, width=20, bd=1)
b_text.place(x=170, y=120)

# Add Button : button()
add_btn = tk.Button(frame, text="Add", padx=25,
                    pady=5, bg="#263d42", fg="white", command=add)
add_btn.place(x=50, y=170)

# Add Button : button()
clear_btn = tk.Button(frame, text="Clear", padx=25,
                      pady=5, bg="#263d42", fg="white", command=clear_data)
clear_btn.place(x=170, y=170)

# Label
lbl_ans = tk.Label(frame, text="", bg="#263d42", fg="white",)
lbl_ans.place(x=80, y=120)

root.mainloop()
