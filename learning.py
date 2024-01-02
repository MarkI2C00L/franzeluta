from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

def button_cmd():
    if not entry.get():
        label_2.configure(text="Type Your Awnser!")
    elif entry.get() == "Moldova":
        label_2.configure(text="You got it right!")
    else:
        label_2.configure(text="Wrong or its not even an country")

root = customtkinter.CTk()
root.title("Mark App")
root.geometry("500x500")
root.resizable(width=False, height=False)

frame = customtkinter.CTkFrame(root, width=400, height=400, corner_radius=32)
frame.pack(padx=20, pady=20)

label = customtkinter.CTkLabel(frame, text="Guess The Country!", font=("Arial", 18, 'bold'))
label.pack(padx=20, pady=20)

entry = customtkinter.CTkEntry(frame, placeholder_text="Country Here!", text_color="white", corner_radius=32)
entry.pack(padx=20, pady=20)

button = customtkinter.CTkButton(frame, text="Guess!", corner_radius=32, command=button_cmd)
button.pack(padx=20, pady=20)

label_2 = customtkinter.CTkLabel(frame, width=200, height=50, fg_color="transparent", text="", font=("Arial", 18, 'bold'))
label_2.pack(padx=20, pady=20)

root.mainloop()