def extract_individual_ids(input_csv, output_csv):
    try:
        # Read the CSV file
        with open(input_csv, 'r') as file:
            lines = file.readlines()
        print("Step 1: Read CSV file - Success")
    except Exception as e:
        print(f"Step 1: Read CSV file - Error: {e}")
        return

    try:
        # Extract the header and data
        header = lines[0].strip().split(',')
        data = [line.strip().split(',') for line in lines[1:]]
        print("Step 2: Extract header and data - Success")
    except Exception as e:
        print(f"Step 2: Extract header and data - Error: {e}")
        return

    try:
        # Find the index of the "Individual ID" column
        individual_id_idx = header.index('Clutch Completion')
        print("Step 3: Find column index - Success")
    except Exception as e:
        print(f"Step 3: Find column index - Error: {e}")
        return

    try:
        # Extract "Individual ID" values and create a tuple
        individual_ids = tuple(row[individual_id_idx] for row in data if len(row) > individual_id_idx and row[individual_id_idx])
        print("Step 4: Extract Individual IDs and create tuple - Success")
    except Exception as e:
        print(f"Step 4: Extract Individual IDs and create tuple - Error: {e}")
        return

    try:
        # Print the output file path
        print(f"Step 5: Writing to output file: {output_csv}")
        
        # Write the tuple to a new CSV file
        with open(output_csv, 'w') as file:
            file.write('Individual IDs\n')
            file.write(','.join(individual_ids))
        print("Step 5: Write to CSV file - Success")
    except Exception as e:
        print(f"Step 5: Write to CSV file - Error: {e}")

# Example usage
extract_individual_ids('palmerpenguins_litter.csv', 'individual_ids.csv')