import csv

def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    f = open(data, 'r')
    reader = csv.reader(f)
    row_count = 0
    for row in reader:
        row_count += 1
    return row_count
a = find_number_of_rows("data.csv")
print(a)

# Read the csv file
