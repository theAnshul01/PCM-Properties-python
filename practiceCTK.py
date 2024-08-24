from customtkinter import *
import pandas as pd
import matplotlib.pyplot as plt

def show():
    result_label.configure(text=f"Result: {Atemp.get()}")

# function to plot graph ----> 
def read_excel_data(filename, sheet_name="Sheet1"):
    
    try:
        df = pd.read_excel(filename, sheet_name=sheet_name)
        return df
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

def plot_data(df, x_col, y_col):
    if df is None:
        print("Error: No data found. Please check the file path.")
        return

    plt.plot(df[x_col], df[y_col])
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"Plot of {y_col} vs. {x_col}")
    plt.grid(True)
    plt.show(block = False)

def plotcall():
    # Get user input
    filename = fPath.get()
    xname = xCol.get()
    yname = yCol.get()

    # Check if all input fields have values
    if filename and xname and yname:
        df = read_excel_data(filename)
        plot_data(df, xname, yname)
    else:
        print("Please enter all required fields (file path, x-axis name, and y-axis name).")

app = CTk()
app.geometry("800x600")
app.title("myApp")
app.anchor("center")
# set_appearance_mode("dark")

# Configure the grid layout to make the frames equal in width
app.grid_columnconfigure(0, weight=1)  # Column 0 (frame1)
app.grid_columnconfigure(1, weight=1)  # Column 1 (frame2)


label = CTkLabel(master=app, text="Enter ambient temperature: ")
label.pack(pady=10)
label.place(relx = 0.4, rely= 0.1)
Atemp = CTkEntry(master=app, placeholder_text="Enter Ambient Temperature")
Atemp.pack(pady=10)
Atemp.place(relx = 0.5, rely=0.1)
# Place the frames in the grid layout
frame1 = CTkFrame(master=app, fg_color="#d6d6a9")
frame2 = CTkFrame(master=app, fg_color="#9be8bb")
frame1.grid(row=0, column=0, sticky="nsew", padx=10)  # Fill the entire column
frame2.grid(row=0, column=1, sticky="nsew", padx=10)  # Fill the entire column

# frame1.grid(row = 0, column = 0, rowspan = 8, columnspan = 3, padx = 10, pady = 10)

# frame2.grid(row = 0, column = 3, rowspan = 8, columnspan = 3, padx = 10, pady = 10)

# -----------------------------------------------------------PCM Frame-----------------------------------------------------------------/

frame1Title = CTkLabel(master=frame1, text="Phase Changing Material Dataset", text_color="black", font=("Arial", 14, "bold"))
frame1Title.grid(row=0, column = 2, columnspan = 2, padx=20, pady=10)
# excel filepath - PCM
excelFilePath = CTkLabel(master=frame1, text="Enter Excel File Path: ", text_color="black")
excelFilePath.grid(row=1, column = 0, columnspan = 2, padx = 10, pady = 10)
fPath = CTkEntry(master=frame1, placeholder_text="file path")
fPath.grid(row = 1, column = 2, columnspan = 2, padx = 10, pady=10)
# x col name
xAxisCol = CTkLabel(master=frame1, text="X-axis column name ", text_color="black")
xAxisCol.grid(row=2, column = 0, columnspan = 2, padx = 10, pady = 10)
xCol = CTkEntry(master=frame1, placeholder_text="x col name")
xCol.grid(row = 2, column = 2, columnspan = 2, padx = 10, pady=10)
# y col name
yAxisCol = CTkLabel(master=frame1, text="Y-axis column name ", text_color="black")
yAxisCol.grid(row=3, column = 0, columnspan = 2, padx = 10, pady = 10)
yCol = CTkEntry(master=frame1, placeholder_text="y col name")
yCol.grid(row = 3, column = 2, columnspan = 2, padx = 10, pady=10)



btn1 = CTkButton(master=frame1, text="Plot Graph", corner_radius=20, fg_color="#C850C0", hover_color="#4158D0", command=plotcall)
btn1.grid(row = 2, column = 4, padx=10, pady=10)

# PCM - starting point 3 times and ending point 3 times
nestedFrame1 = CTkFrame(master=frame1, fg_color="#e3a6da")
nestedFrame1.grid(row = 4, column = 1, columnspan = 4, padx = 60, pady = 10)

# PCM -starting points
sPoint1 = CTkLabel(master=nestedFrame1, text="starting point 1", text_color="black")
sPoint1.grid(row = 0, column = 0, columnspan = 2, padx=10, pady=10)
sPt1 = CTkEntry(master=nestedFrame1, placeholder_text="Enter st point 1")
sPt1.grid(row= 0, column=2, padx=10, pady=10)

sPoint2 = CTkLabel(master=nestedFrame1, text="starting point 2", text_color="black")
sPoint2.grid(row = 1, column = 0, columnspan = 2, padx=10, pady=10)
sPt2 = CTkEntry(master=nestedFrame1, placeholder_text="Enter st point 2")
sPt2.grid(row= 1, column=2, padx=10, pady=10)

sPoint3 = CTkLabel(master=nestedFrame1, text="starting point 3", text_color="black")
sPoint3.grid(row = 2, column = 0, columnspan = 2, padx=10, pady=10)
sPt3 = CTkEntry(master=nestedFrame1, placeholder_text="Enter st point 3")
sPt3.grid(row= 2, column=2, padx=10, pady=10)

# pcm - ending points
ePoint1 = CTkLabel(master=nestedFrame1, text="ending point 1", text_color="black")
ePoint1.grid(row = 0, column = 3, columnspan = 2, padx=10, pady=10 )
ePt1 = CTkEntry(master=nestedFrame1, placeholder_text="Ending point 1")
ePt1.grid(row = 0, column=5, padx=10, pady=10)

ePoint2 = CTkLabel(master=nestedFrame1, text="ending point 2", text_color="black")
ePoint2.grid(row = 1, column = 3, columnspan = 2, padx=10, pady=10 )
ePt2 = CTkEntry(master=nestedFrame1, placeholder_text="Ending point 2")
ePt2.grid(row = 1, column=5, padx=10, pady=10)

ePoint3 = CTkLabel(master=nestedFrame1, text="ending point 3", text_color="black")
ePoint3.grid(row = 2, column = 3, columnspan = 2, padx=10, pady=10 )
ePt3 = CTkEntry(master=nestedFrame1, placeholder_text="Ending point 3")
ePt3.grid(row = 2, column=5, padx=10, pady=10)

#----------------------------------------------- reference material frame-------------------------------------------/

frame2Title = CTkLabel(master=frame2, text="Reference Material Dataset", text_color="black", font=("Arial", 14, "bold"))
frame2Title.grid(row=0, column = 1, columnspan = 2, padx=10, pady=10)

# excel filepath - reference
excelFilePathRef = CTkLabel(master=frame2, text="Enter Excel File Path: ", text_color="black")
excelFilePathRef.grid(row=1, column = 0, columnspan = 2, padx = 10, pady = 10)
fPathRef = CTkEntry(master=frame2, placeholder_text="file path")
fPathRef.grid(row = 1, column = 2, columnspan = 2, padx = 10, pady=10)

# x col name
xAxisColRef = CTkLabel(master=frame2, text="X-axis column name ", text_color="black")
xAxisColRef.grid(row=2, column = 0, columnspan = 2, padx = 10, pady = 10)
xColRef = CTkEntry(master=frame2, placeholder_text="x col name")
xColRef.grid(row = 2, column = 2, columnspan = 2, padx = 10, pady=10)
# y col name
yAxisColRef = CTkLabel(master=frame2, text="Y-axis column name ", text_color="black")
yAxisColRef.grid(row=3, column = 0, columnspan = 2, padx = 10, pady = 10)
yColRef = CTkEntry(master=frame2, placeholder_text="x col name")
yColRef.grid(row = 3, column = 2, columnspan = 2, padx = 10, pady=10)

# REF - starting point 3 times and ending point 3 times
nestedFrame2 = CTkFrame(master=frame2, fg_color="#e3a6da")
nestedFrame2.grid(row = 4, column = 0, columnspan = 4, padx = 10, pady = 10)

# REF -starting points
sPoint1 = CTkLabel(master=nestedFrame2, text="starting point 1", text_color="black")
sPoint1.grid(row = 0, column = 0, columnspan = 2, padx=10, pady=10)
sPt1 = CTkEntry(master=nestedFrame2, placeholder_text="Enter st point 1")
sPt1.grid(row= 0, column=2, padx=10, pady=10)

sPoint2 = CTkLabel(master=nestedFrame2, text="starting point 2", text_color="black")
sPoint2.grid(row = 1, column = 0, columnspan = 2, padx=10, pady=10)
sPt2 = CTkEntry(master=nestedFrame2, placeholder_text="Enter st point 2")
sPt2.grid(row= 1, column=2, padx=10, pady=10)

# REF - ending points
ePoint1 = CTkLabel(master=nestedFrame2, text="ending point 1", text_color="black")
ePoint1.grid(row = 0, column = 3, columnspan = 2, padx=10, pady=10 )
ePt1 = CTkEntry(master=nestedFrame2, placeholder_text="Ending point 1")
ePt1.grid(row = 0, column=5, padx=10, pady=10)

ePoint2 = CTkLabel(master=nestedFrame2, text="ending point 2", text_color="black")
ePoint2.grid(row = 1, column = 3, columnspan = 2, padx=10, pady=10 )
ePt2 = CTkEntry(master=nestedFrame2, placeholder_text="Ending point 2")
ePt2.grid(row = 1, column=5, padx=10, pady=10)


# -------------------------------Result Frame ------------------------//
result_label = CTkLabel(app, text="")
result_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

btn = CTkButton(master=app, text = "Click Me", corner_radius=32, fg_color="#C850C0", hover_color="#4158D0", command=show)
# btn.place(relx=0.5, rely=0.5, anchor="center")


app.mainloop()

