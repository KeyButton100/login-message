from tkinter import *
import time
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
root=Tk()
root.geometry("400x340")
root.title("Secure Login")
root.resizable(False, True)

def abc():
    data=e.get()
    print(n.get())
    result.config(text=data)
    e.delete(0, END)
    p["value"]+=10

Label(text="Username:").pack(pady=10)
e=Entry(root, width=15, font=(20))
e.pack(pady=10)
Label(text="Password:").pack(pady=10)
e=Entry(root, width=15, font=(20))
e.pack(pady=10)
def display():
    messagebox.showinfo("Login Success", "Welcome, [username]!")
Button(root, text="Login", command=display).pack()
result=Label(root, text="")
result.pack()

root.mainloop()