import tkinter as tk
import datetime
from tkinter import filedialog, Text
import os

root=tk.Tk()
root.state('zoomed')
files=[]

def z():
    for widget in frame.winfo_children():
        widget.destroy()
    fielname=filedialog.askopenfilename(initialdir="/",title="Choose file",filetypes=(("Text","*.txt"),("Documents","*.docx"),("All files","*.*"),("Executables","*.exe")))
    files.append(fielname)
    for fil in files:
        label=tk.Label(frame,text=fil,bg="gray")
        label.pack()
        os.startfile(fil)

def y():
    z=filedialog.asksaveasfile(defaultextension=".txt",title="Save as",filetypes=(("Text","*.txt"),("Documents","*.docx"),("EXE","*.exe")))
    filetext=str(text.get(1.0,tk.END))
    z.write(filetext)
    z.close()
    

root.title("FileX")
canvas=tk.Canvas(root,height=700,width=700,bg="black")
canvas.pack(fill="both",expand=True) 
frame=tk.Frame(root,bg="blue")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
text=Text(frame)
text.pack(anchor="n")
openFile=tk.Button(root,text="OPEN",padx=10,pady=4,fg="white",bg="black", command=z)
openFile.pack(anchor="center",fill="x")
runapp=tk.Button(root,text="SAVE",padx=10,pady=4,fg="white",bg="black",command=y)
runapp.pack(fill="x")
root.mainloop()

