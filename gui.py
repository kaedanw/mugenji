# Import GUI Module and Core Program
import tkinter as tk
import core
# import subprocess


# GUI - MugenJi Application
def GUI():
    # Run Core and Assess Return Value
    def core_Input(event):
        userInput = core.user_choice(ent_userInput.get())
        ent_userInput.delete(0, "end")
        if userInput == "Q":
            lbl_entOutput["text"] = f"[{userInput}]: Quit"
            window.destroy()
        elif userInput == "O":
            lbl_entOutput["text"] = f"[{userInput}]: Open List"
        elif userInput == "C":
            lbl_entOutput["text"] = f"[{userInput}]: Clear List"
        elif userInput == "P":
            lbl_entOutput["text"] = f"[{userInput}]: Edit List"
            window.destroy()
            # from subprocess import Popen
            # subprocess.Popen('python guitxt.py')
            GUITXT()
        else:
            lbl_entOutput["text"] = userInput

        
    # Define Application Window
    window = tk.Tk()
    window.title("MugenJi")
    canvas = tk.Canvas(window, width = 300, height = 300)
    # button1 = tk.Button(text='Click Me',command=hello, bg='brown',fg='white')


    # Title
    lbl_title = tk.Label(window, text= 'MugenJi: Word Randomiser', fg='dark red', font=('helvetica', 12, 'bold'))
    canvas.create_window(150, 15, window=lbl_title)


    # Intro Message
    lbl_introTitle = tk.Label(window, text= core.introTitle, fg='black', font=('helvetica', 9, 'bold'))
    canvas.create_window(50, 70, window=lbl_introTitle)
    lbl_introMessage = tk.Label(window, text= core.introMessage, fg='black', font=('helvetica', 9), justify= tk.LEFT)
    canvas.create_window(150, 110, window=lbl_introMessage)


    # Input Entry
    ent_userInput = tk.Entry(window, fg='green', font=('helvetica', 12, 'bold'))
    canvas.create_window(150, 150, window=ent_userInput)
    ent_userInput.focus()
    ent_userInput.bind("<Return>", core_Input)


    # Output
    lbl_entOutput = tk.Label(window, text= "", fg='black', font=('helvetica', 9, 'bold'), justify= tk.LEFT, anchor= "s", wraplength= "150")
    canvas.create_window(150, 200, window=lbl_entOutput)


    # Draw Features
    canvas.pack()
    window.mainloop()


# GUITXT - edit window
def GUITXT():
    def on_close():
        txtWindow.destroy()
        GUI()

    def save_list():
        with open("MugenList.txt", "w") as output_file:
            text = txt_edit.get(1.0, "end-1c")
            output_file.write(text)
        txtWindow.destroy()
        GUI()
        
    txtWindow = tk.Tk()
    txtWindow.title("Mugen List")
    txtWindow.rowconfigure(0, minsize=600, weight=1)
    txtWindow.columnconfigure(1, minsize=100, weight=1)

    txt_edit = tk.Text(txtWindow)
    fr_buttons = tk.Frame(txtWindow, relief=tk.RAISED, bd=2)
    btn_save = tk.Button(fr_buttons, text="Save", command=save_list)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5)
    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")

    with open("MugenList.txt", "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)

    txtWindow.protocol("WM_DELETE_WINDOW",  on_close)
    txtWindow.mainloop()


# Run GUI
GUI()