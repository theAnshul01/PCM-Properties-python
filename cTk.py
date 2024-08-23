from customtkinter import *

# functions
def mutiply():
    value = int(entry.get())*3
    print(f"Returned value: {value}")


app = CTk()
app.geometry("800x600")
app.title("myApp")
set_appearance_mode("dark")

frame = CTkFrame(master = app, fg_color="#8d6f3a")
frame.grid(row = 0, column = 0, rowspan = 4, columnspan=4, padx = 10, pady = 10)
love = CTkFrame(master = app)
love.grid(row = 5, column = 0, rowspan = 2, columnspan=4,padx = 0, pady = 10)

label = CTkLabel(master=frame, text="test tube mass: ", font=("Verdana", 18))
label.grid(row = 0, column = 0, padx = 10, pady = 10)
label = CTkLabel(master=frame, text="another mass: " , font=("Verdana", 18))
label.grid(row = 1, column = 0, padx = 10)
entry = CTkEntry(master=frame, placeholder_text="Enter mass of test tube",)
entry.grid(row = 0, column = 1, padx = 10, pady = 10)

# # text
# label = CTkLabel(master=app, text="Some Text...", font=("Verdana", 12))

# label.pack(pady=10)
# label.place(relx=0.05, rely=0.05)
# entry = CTkEntry(master=app, placeholder_text="Enter mass of test tube",)
# entry.place(relx=0.1, rely=0.1)
# entry.pack(pady=20)
# entry = CTkEntry(master=app, placeholder_text="Water mass" )
# entry.place(relx=0.1, rely=0.2)
# # buttons
# btn = CTkButton(master=app, text = "Click Me", corner_radius=32, fg_color="#C850C0", hover_color="#4158D0", command=mutiply)

# btn.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()










































# import customtkinter

# def button_callback():
#     print("button pressed")

# app = customtkinter.CTk()
# app.title("my app")
# app.geometry("800x600")

# # entry = customtkinter.CTkEntry(app, placeholder_text="CTKEntry")
# label = customtkinter.CTkLabel(app, text="CTkLabel", font=("Arial", 20), text_color="#FFCC70")

# button = customtkinter.CTkButton(app, text="Sign Up", command=button_callback)
# button.place(relx=0.5, rely=0.5, anchor="center")
# # button.grid(row=0, column=0, padx=20, pady=20)

# app.mainloop()