

# Function to parse the date from the CSV line
def parse_date(line):
    # Assuming the date is in the second column (index 1) and in the format 'YYYY-MM-DD'
    columns = line.strip().split(',')
    return columns[9]

# Read the CSV file and find the range of hatch dates
with open(r'C:\Users\trash\OneDrive\Data science\palmerpenguins_litter.csv', 'r') as file:
    # Skip the header line
    next(file)
    
    # Initialize variables to store the earliest and latest dates
    earliest_date = None
    latest_date = None
    
    for line in file:
        date = parse_date(line)
        
        if earliest_date is None or date < earliest_date:
            earliest_date = date
        
        if latest_date is None or date > latest_date:
            latest_date = date

# Print the range of hatch dates
print("Earliest Hatch Date:", earliest_date)
print("Latest Hatch Date:", latest_date)
Range=(earliest_date,latest_date)
print("Range of hatch dates:",Range)
