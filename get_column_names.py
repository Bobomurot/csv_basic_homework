#Define function,Get coloumn names from a csv file
import csv

def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    f = open(data, 'r')
    reader = csv.reader(f)
    for columns in reader:
        return columns
    return []
a = get_column_names("data.csv")
print(a)
    
# Read the csv file