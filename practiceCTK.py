from customtkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from numpy import trapz 

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

def calculate_area_under_curve(df, x_col, y_col, start_point, end_point):
    """Calculates the area under the curve between specified points.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data.
        x_col (str): Name of the column for the x-axis.
        y_col (str): Name of the column for the y-axis.
        start_point (float): X-coordinate of the starting point.
        end_point (float): X-coordinate of the ending point.

    Returns:
        float: The area under the curve between the points.
    """

    x = df[x_col].to_numpy()
    y = df[y_col].to_numpy()
    mask = (x >= start_point) & (x <= end_point)  # Filter data within points
    return trapz(y[mask], x[mask])

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

#  plot graph for reference
def plotcall2():
    # Get user input
    filename = fPathRef.get()
    xname = xColRef.get()
    yname = yColRef.get()
    # Check if all input fields have values
    if filename and xname and yname:
        df = read_excel_data(filename)
        plot_data(df, xname, yname)
    else:
        print("Please enter all required fields (file path, x-axis name, and y-axis name).")

# ! Area calculation
# area = calculate_area_under_curve(df, x_col, y_col, start_point, end_point) - ((end_point-start_point)*ambientTemp)
def calcArea1():
    s1 = sPt1.get() 
    s2 = sPt2.get()
    s3 = sPt3.get()
    
    e1 = ePt1.get()
    e2 = ePt2.get()
    e3 = ePt3.get()
    filename = fPath.get()
    # filename = 'FYP-Readings.xlsx'
    xname = xCol.get()
    yname = yCol.get()
    A1 = 0
    if filename:
        df = read_excel_data(filename)
        # if s1 and e1:
        #     A1 = calculate_area_under_curve(df, xname, yname, int(s1), int(e1))
        # else:
        #     print("s1 or e1 is empty")
        A1 = calculate_area_under_curve(df, xname, yname, int(s1), int(e1)) - ((int(e1)-int(s1))*int(Atemp.get()))
        A2 = calculate_area_under_curve(df, xname, yname, int(s2), int(e2)) - ((int(e2)-int(s2))*int(Atemp.get()))
        A3 = calculate_area_under_curve(df, xname, yname, int(s3), int(e3)) - ((int(e3)-int(s3))*int(Atemp.get()))
        areaLabel1.configure(text=f"Area: {A1:.2f}")
        areaLabel2.configure(text=f"Area: {A2:.2f}")
        areaLabel3.configure(text=f"Area: {A3:.2f}")
    else:
        print("file name isn't available")


app = CTk()
app.geometry("1000x400")
app.title("myApp")
app.anchor("center")
# set_appearance_mode("dark")


#! Have changed this
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
# ! Removed stickyness
frame1 = CTkFrame(master=app, fg_color="#d6d6a9", height=500)
frame2 = CTkFrame(master=app, fg_color="#9be8bb", height=500) 
frame1.grid(row=0, column=0,  padx=10)  # Fill the entire column
frame2.grid(row=0, column=1, padx=10, pady=10)  # Fill the entire column

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

btn1 = CTkButton(master=nestedFrame1, text="Calculate Area", corner_radius=20, fg_color="#C850C0", hover_color="#4158D0", command=calcArea1)
btn1.grid(row = 1, column = 6, padx=10, pady=10)

areaLabel1 = CTkLabel(master=nestedFrame1, text="")
areaLabel1.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
areaLabel2 = CTkLabel(master=nestedFrame1, text="")
areaLabel2.grid(row=3, column=2, columnspan=2, padx=10, pady=10)
areaLabel3 = CTkLabel(master=nestedFrame1, text="")
areaLabel3.grid(row=3, column=4, columnspan=2, padx=10, pady=10)
#----------------------------------------------- reference material frame-------------------------------------------/

frame2Title = CTkLabel(master=frame2, text="Reference Material Dataset", text_color="black", font=("Arial", 14, "bold"))
frame2Title.grid(row=0, column = 1, columnspan = 3, padx=10, pady=10)

# excel filepath - reference
excelFilePathRef = CTkLabel(master=frame2, text="Enter Excel File Path: ", text_color="black")
excelFilePathRef.grid(row=1, column = 0, padx = 10, pady = 10)
fPathRef = CTkEntry(master=frame2, placeholder_text="file path")
fPathRef.grid(row = 1, column = 1, columnspan = 2, padx = 10, pady=10)

# x col name
xAxisColRef = CTkLabel(master=frame2, text="X-axis column name ", text_color="black")
xAxisColRef.grid(row=2, column = 0, padx = 10, pady = 10)
xColRef = CTkEntry(master=frame2, placeholder_text="x col name")
xColRef.grid(row = 2, column = 1, columnspan = 2, padx = 10, pady=10)
# y col name
yAxisColRef = CTkLabel(master=frame2, text="Y-axis column name ", text_color="black")
yAxisColRef.grid(row=3, column = 0, padx = 10, pady = 10)
yColRef = CTkEntry(master=frame2, placeholder_text="x col name")
yColRef.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady=10)

btn2 = CTkButton(master=frame2, text="Plot Graph", corner_radius=20, fg_color="#C850C0", hover_color="#4158D0", command=plotcall2)
btn2.grid(row = 2, column = 3, padx=10, pady=10)

# REF - starting point 3 times and ending point 3 times
nestedFrame2 = CTkFrame(master=frame2, fg_color="#e3a6da")
nestedFrame2.grid(row = 4, column = 0, columnspan = 4, padx = 10, pady = 10)

# REF -starting points
sPoint1 = CTkLabel(master=nestedFrame2, text="starting point 1", text_color="black")
sPoint1.grid(row = 0, column = 0, columnspan = 2, padx=10, pady=10)
sPtRef1 = CTkEntry(master=nestedFrame2, placeholder_text="Enter st point 1")
sPtRef1.grid(row= 0, column=2, padx=10, pady=10)

sPoint2 = CTkLabel(master=nestedFrame2, text="starting point 2", text_color="black")
sPoint2.grid(row = 1, column = 0, columnspan = 2, padx=10, pady=10)
sPtRef2 = CTkEntry(master=nestedFrame2, placeholder_text="Enter st point 2")
sPtRef2.grid(row= 1, column=2, padx=10, pady=10)

# REF - ending points
ePoint1 = CTkLabel(master=nestedFrame2, text="ending point 1", text_color="black")
ePoint1.grid(row = 0, column = 3, columnspan = 2, padx=10, pady=10 )
ePtRef1 = CTkEntry(master=nestedFrame2, placeholder_text="Ending point 1")
ePtRef1.grid(row = 0, column=5, padx=10, pady=10)

ePoint2 = CTkLabel(master=nestedFrame2, text="ending point 2", text_color="black")
ePoint2.grid(row = 1, column = 3, columnspan = 2, padx=10, pady=10 )
ePtRef2 = CTkEntry(master=nestedFrame2, placeholder_text="Ending point 2")
ePtRef2.grid(row = 1, column=5, padx=10, pady=10)

btn2 = CTkButton(master=nestedFrame2, text="Calculate Area", corner_radius=20, fg_color="#C850C0", hover_color="#4158D0")
btn2.grid(row = 0, column = 6, padx=10, pady=10)

# areaLabel1 = CTkLabel(master=nestedFrame1, text="")
# areaLabel1.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
# areaLabel2 = CTkLabel(master=nestedFrame1, text="")
# areaLabel2.grid(row=3, column=2, columnspan=2, padx=10, pady=10)
# areaLabel3 = CTkLabel(master=nestedFrame1, text="")
# areaLabel3.grid(row=3, column=4, columnspan=2, padx=10, pady=10)


# -------------------------------Result Frame ------------------------//
result_label = CTkLabel(app, text="")
result_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

btn = CTkButton(master=app, text = "Click Me", corner_radius=32, fg_color="#C850C0", hover_color="#4158D0", command=show)
# btn.place(relx=0.5, rely=0.5, anchor="center")


app.mainloop()

