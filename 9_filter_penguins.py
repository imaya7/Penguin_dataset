def filter_penguins(input_csv, output_csv, min_body_mass, min_flipper_length):
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
        # Find the indices of the required columns
        body_mass_idx = header.index('body_mass_g')
        flipper_length_idx = header.index('flipper_length_mm')
        print("Step 3: Find column indices - Success")
    except Exception as e:
        print(f"Step 3: Find column indices - Error: {e}")
        return

    try:
        # Filter penguins based on the specified criteria
        filtered_penguins_2 = [
            row for row in data
            if row[body_mass_idx] != 'NA' and row[flipper_length_idx] != 'NA' and
               float(row[body_mass_idx]) > min_body_mass and float(row[flipper_length_idx]) > min_flipper_length
        ]
        print("Step 4: Filter penguins - Success")
    except Exception as e:
        print(f"Step 4: Filter penguins - Error: {e}")
        return

    try:
        # Write the filtered list to a new CSV file
        with open(output_csv, 'w') as file:
            file.write(','.join(header) + '\n')
            for row in filtered_penguins_2:
                file.write(','.join(row) + '\n')
        print("Step 5: Write to CSV file - Success")
    except Exception as e:
        print(f"Step 5: Write to CSV file - Error: {e}")

# Example usage
filter_penguins('palmerpenguins_size.cvs.csv', 'filtered_penguins_2.csv', 4000, 190)