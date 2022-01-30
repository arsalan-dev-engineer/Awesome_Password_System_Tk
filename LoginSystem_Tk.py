from tkinter import *
import tkinter.messagebox

window = Tk()
# global variable, used for while loop inside the authenticator function
attempts = 5


def authenticator():
    """Function will authenticate user input and if conditions == "Admin",
     system will authenticate and close current window, if attempts are 0,
     system entries will be set as disabled"""
    # call variable from ouside function
    global attempts
    while attempts > 0:
        if (lgnName_Entry.get() == "Admin") and (lgnPass_Entry.get() == "Admin"):
            tkinter.messagebox.showinfo("Login", f"Login Successful")
            # button will change colour to green if login successful
            submitBtn.configure(bg="#33cc33")
            # entries will be disabled
            lgnName_Entry.configure(state="disabled")
            lgnPass_Entry.configure(state="disabled")
            break
            

        elif (lgnName_Entry.get() != "Admin") or (lgnPass_Entry.get() != "Admin"):
            tkinter.messagebox.showwarning("Login Error", "Incorrect Password")
            
            # attempts remaining label
            remaining_Label = Label(window, text="Attempts remaining:")
            remaining_Label.place(x=106, y=145)
            # number of attempts left will be displayed
            attempts_Label = Label(window, text=attempts-1)
            attempts_Label.place(x=220, y=146)
            # decrement attempts variable
            attempts -= 1
            break
        
    if attempts == 0:
        # message box once attempts equals to 0 from 5
        tkinter.messagebox.showwarning("Too many attempts", "System locked, please restart program")
        # attempts label and button will change colour to dark red
        attempts_Label.configure(fg="#b30000")
        submitBtn.configure(bg="#b30000")
        # username and password entries will be locked
        lgnName_Entry.configure(state="disabled")
        lgnPass_Entry.configure(state="disabled")
    

# login label
lgnLabel = Label(window, text="Enter Login Details")
lgnLabel.place(x=110, y=60)

# username
lgnName_Label = Label(window, text="Username")
lgnName_Label.place(x=45, y=90)

# password
lgnPass_Label = Label(window, text="Password")
lgnPass_Label.place(x=45, y=120)

# username entry
lgnName_Entry = Entry(window, width=35)
lgnName_Entry.place(x=110, y=90)

# password entry
lgnPass_Entry = Entry(window, width=35, show="*")
lgnPass_Entry.place(x=110, y=120)

# submit button
submitBtn = Button(window, text="Log In", width=15, height=2, bg="#80ccff", command=authenticator)
submitBtn.place(x=109, y=174)

# window configurations/features
window.title("Azzy001 : https://github.com/Azzy001")
window.geometry("380x400")
window.resizable(0, 0)
window.attributes("-topmost", True)
window.mainloop()
