import customtkinter

import AutoSaveLogic

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("600x500")
app.resizable(False, False)
app.title("Server Auto Save")


#def button_callback():
#   print("Button Clicked, Fun times ahead")
    
def backup_button():
    AutoSaveLogic.SetServerPath(directorypath.get(), WriteToTextBox, backupPath.get())
    AutoSaveLogic.GetImportantFiles(WriteToTextBox)
    print("Making Backup")
    
def game_dropdown(choice):
    print("Game chosen: ", choice)
    AutoSaveLogic.SetGame(choice)
    
def WriteToTextBox(text):
    textbox.configure(state="normal")
    textbox.insert("end", text)
    textbox.configure(state="disabled")

#Order of the .pack() call decides what goes on top

pathFrame = customtkinter.CTkFrame(master=app, width=600, height=200, fg_color="transparent")
pathFrame.pack(pady=10, padx=10)

#Input for Server Directory
directorypath = customtkinter.CTkEntry(master=pathFrame, placeholder_text="Path to Server", width=500)
directorypath.pack(pady=20, padx=10)

backupPath = customtkinter.CTkEntry(master=pathFrame, placeholder_text="Path to Backup", width=500)
backupPath.pack()

frame = customtkinter.CTkFrame(master=app, width=600, height=200, fg_color="transparent")
frame.pack(pady=10, padx=10)

gamedropdown = customtkinter.CTkOptionMenu(master=frame, values=["Vintage Story", "Minecraft", "Arma 3"], command=game_dropdown)
gamedropdown.pack(pady=10, padx=10, side="left")
gamedropdown.set("Games") #Set is a method to label the widget

button = customtkinter.CTkButton(master=frame, text="Back up server", command=backup_button)
#button.grid(row=0,column=0)
button.pack(pady=20, padx=10, side="right") #positon in the window

#Used to display when back up is finished or in progress and all back up zip files
textbox = customtkinter.CTkTextbox(app, width=500)
textbox.pack(pady=10, padx=10)
textbox.insert("0.0", "Log:\n")
textbox.configure(state="disabled")

app.mainloop()