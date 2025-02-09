import csv

def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    f = open(data, 'r')
    reader = csv.reader(f)
    first_column = []
    for column in reader:
        if column:
            first_column.append(column[0])
    return first_column
a = get_first_column("data.csv")
print(a)
    
# Read the csv file