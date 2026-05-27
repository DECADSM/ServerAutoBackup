import customtkinter

import AutoSaveLogic

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("1280x720")
app.title("Server Auto Save")


#def button_callback():
#   print("Button Clicked, Fun times ahead")
    
def backup_button():
    print("Making Backup")
    
def game_dropdown(choice):
    print("Game chosen: ", choice)
    AutoSaveLogic.SetGame(choice)
    
def WriteToTextBox(textbox, text):
    textbox.configure(state="enabled")
    textbox.insert("end", text)
    textbox.configure(state="disabled")
    
button = customtkinter.CTkButton(app, text="Back up server", command=backup_button)
#button.grid(row=0,column=0)
button.pack(pady=10, padx=10) #positon in the window

gamedropdown = customtkinter.CTkOptionMenu(app, values=["Vintage Story", "Minecraft", "Arma 3"], command=game_dropdown)
gamedropdown.pack(pady=20, padx=20)
gamedropdown.set("Games") #Set is a method to label the widget

#Used to display when back up is finished or in progress and all back up zip files
textbox = customtkinter.CTkTextbox(app)
textbox.pack(pady=30, padx=30)
textbox.insert("0.0", "Log:\n")
textbox.configure(state="disabled")

#Input for Server Directory
directorypath = customtkinter.CTkEntry(app, placeholder_text="Path to Server")
directorypath.pack(pady=40, padx=40)

app.mainloop()