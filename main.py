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

def main():
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
                n = int(input("How many times do you want to calculate the area? "))
                ambientTemp = int(input("Enter the ambient temperature: "))
                for n in range(n):
                    start_point = float(input("Enter the starting point (x-coordinate): "))
                    end_point = float(input("Enter the ending point (x-coordinate): "))
                    area = calculate_area_under_curve(df, x_col, y_col, start_point, end_point) - ((end_point-start_point)*ambientTemp)
                    print(f"Area under the curve between {start_point} and {end_point}: {area:.2f}")  # Format area with 2 decimal places
            except ValueError:
                print("Invalid input. Please enter numbers for start and end points.")

        #
                
main()
