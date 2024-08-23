import pandas as pd
import matplotlib.pyplot as plt
from numpy import trapz  # For calculating area under the curve

def read_excel_data(filename, sheet_name="Sheet1"):
    """Reads data from an Excel file into a pandas DataFrame.

    Args:
        filename (str): Path to the Excel file.
        sheet_name (str, optional): Name of the sheet to read. Defaults to "Sheet1".

    Returns:
        pandas.DataFrame: The data from the specified sheet.
    """

    try:
        df = pd.read_excel(filename, sheet_name=sheet_name)
        return df
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

def plot_data(df, x_col, y_col):
    """Plots the data from a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data.
        x_col (str): Name of the column for the x-axis.
        y_col (str): Name of the column for the y-axis.
    """

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

def perform_custom_calculations(df, formulas):
    """Performs calculations using user-provided formulas.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data.
        formulas (dict): Dictionary where keys are column names and values are formulas.

    Returns:
        pandas.DataFrame: The DataFrame with new columns containing the calculated results.
    """

    new_cols = []
    for col_name, formula in formulas.items():
        df[col_name] = eval(formula)  # Evaluate formula using the DataFrame
        new_cols.append(col_name)
    return df[new_cols]  # Return only the newly created columns

# --------Area calculation for PCM material--------------//
def PCM(areaList1, ambientTemp):
    """Main function to handle user input and perform operations."""

    filename = input("Enter the Excel file path: ")
    df = read_excel_data(filename)

    if df is not None:
        # Get column names
        x_col = input("Enter the column name for the x-axis: ")
        y_col = input("Enter the column name for the y-axis: ")

        # Plot the data
        plot_data(df, x_col, y_col)

        # Calculate area under the curve (optional)
        choice = input("Do you want to calculate the area under the curve (y/n)? ")
        if choice.lower() == "y":
            try:
                # ambientTemp = int(input("Enter the ambient temperature: "))
                for n in range(3):
                    start_point = float(input("Enter the starting point (x-coordinate): "))
                    end_point = float(input("Enter the ending point (x-coordinate): "))
                    area = calculate_area_under_curve(df, x_col, y_col, start_point, end_point) - ((end_point-start_point)*ambientTemp)
                    areaList1.append(round(area,2))
                    print(f"Area under the curve between {start_point} and {end_point}: {area:.2f}")  # Format area with 2 decimal places
            except ValueError:
                print("Invalid input. Please enter numbers for start and end points.")
        # print(areaList1)
        #

# ------------Area calculation for water-------------//
def water(areaList2, ambientTemp):
    """Main function to handle user input and perform operations."""

    filename = input("Enter the Excel file path: ")
    df = read_excel_data(filename)

    if df is not None:
        # Get column names
        x_col = input("Enter the column name for the x-axis: ")
        y_col = input("Enter the column name for the y-axis: ")

        # Plot the data
        plot_data(df, x_col, y_col)

        # Calculate area under the curve (optional)
        choice = input("Do you want to calculate the area under the curve (y/n)? ")
        if choice.lower() == "y":
            try:
                # ambientTemp = int(input("Enter the ambient temperature: "))
                for n in range(2):
                    start_point = float(input("Enter the starting point (x-coordinate): "))
                    end_point = float(input("Enter the ending point (x-coordinate): "))
                    area = calculate_area_under_curve(df, x_col, y_col, start_point, end_point) - ((end_point-start_point)*ambientTemp)
                    areaList2.append(round(area,2))
                    # print(f"Area under the curve between {start_point} and {end_point}: {area:.2f}")  # Format area with 2 decimal places
            except ValueError:
                print("Invalid input. Please enter numbers for start and end points.")
        # print(areaList2)
        #

def main():
    areaList1 = []
    areaList2 = []
    ambientTemp = int(input("Enter the ambient temperature: "))
    print("Input data for PCM material")
    PCM(areaList1, ambientTemp)
    print("Input data for water/reference material")
    water(areaList2, ambientTemp)

    # input values - test tube weight, PCM weight, water weight, Cp of water,
    TT_Weight = float(input("Enter mass of test tube: "))
    PCM_Weight = float(input("Enter mass of PCM material: "))
    water_Weight = float(input("Enter mass of water: "))
    Cp_t = float(input("Enter Cp value of Glass of test tube: "))

    # Cp in solid state
    Cp_s = ((((water_Weight*4.18) + (TT_Weight*Cp_t))/PCM_Weight) *areaList1[2]/areaList2[1]) - ((TT_Weight*Cp_t)/PCM_Weight)
    # Cp in liquid state
    Cp_l = ((((water_Weight*4.18) + (TT_Weight*Cp_t))/PCM_Weight) *areaList1[0]/areaList2[0]) - ((TT_Weight*Cp_t)/PCM_Weight)
    # enthalpy of PCM
    T_init = float(input("Enter initial temperature of PCM: "))
    # two conditions - supercooled or not 
    isSupercooled = input("With supercooling ? YES or NO: ")
    if isSupercooled == "YES" or "yes":
        T_sat = float(input("Enter saturation temp: "))
        Hm = ((((water_Weight*4.18) + (TT_Weight*Cp_t))/PCM_Weight) *areaList1[1]/areaList2[0]) * (T_init - T_sat)
    else:
        T_m1 = float(input("Enter Tm1 temp: "))
        T_m2 = T_m1 - 6
        Hm = ((((water_Weight*4.18) + (TT_Weight*Cp_t))/PCM_Weight) *areaList1[1]/areaList2[0]) * (T_init - T_m1) - (TT_Weight*Cp_t*(T_m1 - T_m2))/PCM_Weight

    print("Cps: ", round(Cp_s,3))
    print("Cpl: ", round(Cp_l,3))
    print("Hm: ", Hm)
           
main()
