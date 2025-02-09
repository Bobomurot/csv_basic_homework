import csv
def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   f = open(data, 'r')
   reader = csv.reader(f)
   row_count = 0
   for row in reader:
       row_count += 1
       if row_count == 2:
           return row
   return []
a = get_first_row("data.csv")
print(a)



# Read the csv file