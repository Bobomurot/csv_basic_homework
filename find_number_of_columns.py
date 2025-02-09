import csv
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    f = open(data, 'r')
    reader = csv.reader(f)
    
    for columns in reader:
        return len(columns)
    return 0
a = find_number_of_columns("data.csv")
print(a)



# Read the csv file