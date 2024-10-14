import csv
from collections import defaultdict
from datetime import datetime

def calculate_clutch_completion_rate(file_path):
    # Initialize data structures
    region_year_data = defaultdict(lambda: defaultdict(list))
    
    # Read the CSV file
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            region = row['Region']
            clutch_completion = row['Clutch Completion']
            date_egg = row['Date Egg']
            
            # Extract year from date
            try:
                year = datetime.strptime(date_egg, '%m/%d/%Y').year
            except ValueError:
                continue  # Skip rows with invalid date format
            
            # Convert Clutch Completion to a boolean value
            clutch_completion_value = 1 if clutch_completion.lower() == 'yes' else 0
            
            # Append the clutch completion value to the corresponding region and year
            region_year_data[region][year].append(clutch_completion_value)
    
    # Calculate average clutch completion rate for each region per year
    average_clutch_completion_rate = {}
    for region, years in region_year_data.items():
        average_clutch_completion_rate[region] = {}
        for year, completions in years.items():
            average_clutch_completion_rate[region][year] = sum(completions) / len(completions)
    
    return average_clutch_completion_rate

# Example usage
file_path = 'palmerpenguins_litter.csv'
average_rates = calculate_clutch_completion_rate(file_path)
for region, years in average_rates.items():
    for year, rate in years.items():
        print(f'Region: {region}, Year: {year}, Average Clutch Completion Rate: {rate:.2f}')