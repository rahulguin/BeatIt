from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog as fd
from ChordInference import ChordInference

root = Tk()
root.title("BeatIt")
root.geometry('600x300')



def open_file():
    fileName = fd.askopenfilename()
    model = ChordInference()
    if fileName is not None:
        observations = model.extractPitch(fileName)
        result = model.generateChords(observations)
        model.generateOutputFile(result)



btnOpen = Button(root, text='Open', command=lambda: open_file(), activebackground = "#33B5E5")
btnOpen.pack(side=TOP, pady=10)

root.mainloop()