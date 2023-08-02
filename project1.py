from tkinter import *

# widgets = GUI elements: buttons, textboxes, lables, images
# windows = serves as a container to hold or contain these widgets

window = Tk() #instantiate an instance of a window

window.geometry("420*420")
window.title("yvonne my first GUI program!")

icon = PhotoImage(file='gold.png')
window.iconphoto(True,icon)
window.config(background="#5cfcff")

window.mainloop() #place window on computer screen, listens for events.
