from tkinter import *
from tkinter import messagebox 
window =Tk()
window.geometry("900x500")
window.title("registration form")
window.configure (bg="pink")
def registration():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    if name and email and password:
        messagebox.showinfo("registration successful","Thankyou for registering!")
    else:
        messagebox.showerror("error","pleace fill the all fields.")
label_name = Label(window,text="  name:")
label_name.place(x=100, y=70)
entry_name = Entry(window)
entry_name.place(x=200, y=70)

label_email = Label(window,text="  email:")
label_email.place(x=100, y=90)
entry_email = Entry(window)
entry_email.place(x=200, y=90)

label_password = Label(window,text="password:")
label_password.place(x=100, y=110)
entry_password = Entry(window,show="*")
entry_password.place(x=200, y=110)

submit_button = Button(window,text="register",command=registration)
submit_button.place(x=200, y=150)
window.mainloop()