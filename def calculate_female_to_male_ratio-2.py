def calculate_female_to_male_ratio(file_path):
    # This function checks the ration of male to female penguins on each island
    # Initialize dictionaries to count females and males per island
    female_count = {}
    male_count = {}
    
    try:
        # Read the CSV file
        with open(file_path, 'r') as file:
            # Skip the header line
            header = file.readline()
            
            # Process each row
            for line in file:
                columns = line.strip().split(',')
                if len(columns) < 15:
                    print(f"Skipping malformed line: {line.strip()}")
                    continue
                
                island = columns[4]
                sex = columns[14].upper()  # Ensure case insensitivity
                
                if sex == 'FEMALE':
                    if island in female_count:
                        female_count[island] += 1
                    else:
                        female_count[island] = 1
                elif sex == 'MALE':
                    if island in male_count:
                        male_count[island] += 1
                    else:
                        male_count[island] = 1
        
        # Calculate the female to male ratio for each island
        ratio = {}
        for island in female_count:
            females = female_count[island]
            males = male_count.get(island, 0)
            if males > 0:
                ratio[island] = f"{females}:{males}"
            else:
                ratio[island] = f"{females}:0"  # Handle case where there are no males
        
        # Return the results
        return ratio
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
file_path = 'palmerpenguins_litter.csv'
ratios = calculate_female_to_male_ratio(file_path)
if ratios:
    for island, ratio_value in ratios.items():
        print(f"{island}: {ratio_value}")