import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import ttk

# Defines the command to choose a file from a popup window
def choose_file():
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    label.config(text = "%s" % filename)
    build_selection_ui()
    
# Replace with code to read HHC and spit out the real topic list
f = open("test.txt", "r")
topics = f.read()
f.close()
topics_lst = topics.split("\n")

# I put this bit in a class in case that is the key to reading values from option menus generated from a for loop
class Menu_from_File():
    def __init__(self, master, topics_lst):
        self.master = master
        self.topics_lst = topics_lst
        self.create_widgets()
            
    def create_widgets(self):
        # Creates a dropdown for each topic listed in the file
        next_row = 2
        all_menus = []
        for topic in self.topics_lst:
            self.topic_title = topic.partition(",")[0] # Here I take of the ",Concept" bit but I think we could do without that to begin with
            
            self.topic_label = tk.Label(self.master, fg="dark slate gray", bg="SeaGreen1",
                                text = "%s" % self.topic_title)
            self.topic_label.grid(column=0, row=next_row, padx = 20, pady = 10, sticky = tk.W)
            
            OptionList = [
            "                     ",
            "Concept", 
            "Reference",
            "Task"]
            
            self.variable = tk.StringVar(self.master)
            self.variable.set(OptionList[0])
            self.types_menu = ttk.OptionMenu(self.master, self.variable, *OptionList)
            self.types_menu.grid(column=1, row=next_row, padx = 20, pady = 10, sticky = tk.W)
            
            next_row += 1
            
            #Combines the topic title and menu selection in a tuple
            topic_row = (self.topic_title, self.variable)
            #Adds info for each topic to a list
            all_menus.append(topic_row)
           
        # Defines what the Set Topic Types button does
        def get_types():
            typed_topics = []
            for topic in all_menus:
                typed_topics.append((topic[0], topic[1].get()))
            print(typed_topics)
            
        # Defines the Set Topic Types button
        button_row = next_row + len(self.topics_lst)
        set_topic_types = tk.Button(frame_main, bg="thistle2", 
                           text="Set Topic Types",
                           command=get_types)
        set_topic_types.grid(row = button_row, column = 1, padx = 10, pady = 10, sticky = tk.W)

# Defines how to build a bespoke UI from the topic list provided
def build_selection_ui():
    frame_canvas = tk.Frame(frame_main)
    frame_canvas.grid(row=1, column=1, pady=(5, 0), sticky='nw')
    frame_canvas.grid_rowconfigure(0, weight=1)
    frame_canvas.grid_columnconfigure(0, weight=1)

    # Add a canvas in that frame
    canvas = tk.Canvas(frame_canvas)
    canvas.grid(row=0, column=0, sticky="nsew")

    # Link a scrollbar to the canvas
    vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
    vsb.grid(row=0, column=1, sticky='ns')
    canvas.configure(yscrollcommand=vsb.set)

    # Create a frame to contain the menus
    frame_menus = tk.Frame(canvas, bg="SeaGreen1")
    canvas.create_window((0, 0), window=frame_menus, anchor='nw')

    
    # Reads a file to a list. Will need to fill in code to get the actual file Caleb's tool generates
    Menu_from_File(frame_menus, topics_lst)
    # Update buttons frames idle tasks to let tkinter calculate menu sizes
    frame_menus.update_idletasks()
    canvas.config(width=frame_menus.winfo_width())
    canvas.config(scrollregion=canvas.bbox("all"))
     
# Defines the window, I think      
root = tk.Tk()
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame_main = tk.Frame(root, bg="thistle1")
frame_main.grid(sticky='news')

# The windowdow title
root.title("Assign Topic Types")

# Defines and places a label that will show what hhc the user selected
label = tk.Label(frame_main, fg="dark slate gray", bg="thistle1", text = "No HHC Selected")
label.grid(row = 0, column = 1, padx = 20, pady = 10, sticky = tk.W)

# Defines the Select HHC button
hhc = tk.Button(frame_main, bg="thistle2",
                   text="Select HHC",
                   command=choose_file)
hhc.grid(row = 0, column = 0, padx = 20, pady = 10, sticky = tk.W)

# Event loop
root.mainloop()