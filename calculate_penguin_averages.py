def calculate_penguin_averages(input_csv, output_csv):
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
        species_idx = header.index('Species')
        flipper_length_idx = header.index('Flipper Length (mm)')
        body_mass_idx = header.index('Body Mass (g)')
        culmen_length_idx = header.index('Culmen Length (mm)')
        culmen_depth_idx = header.index('Culmen Depth (mm)')
        print("Step 3: Find column indices - Success")
    except Exception as e:
        print(f"Step 3: Find column indices - Error: {e}")
        return

    try:
        # Initialize dictionaries to store sums and counts
        sums = {}
        counts = {}
        print("Step 4: Initialize dictionaries - Success")
    except Exception as e:
        print(f"Step 4: Initialize dictionaries - Error: {e}")
        return

    try:
        # Iterate over the data to calculate sums and counts
        for row in data:
            species = row[species_idx]
            if species not in sums:
                sums[species] = [0, 0, 0, 0]
                counts[species] = 0

            try:
                flipper_length = float(row[flipper_length_idx])
                body_mass = float(row[body_mass_idx])
                culmen_length = float(row[culmen_length_idx])
                culmen_depth = float(row[culmen_depth_idx])
            except ValueError:
                continue

            sums[species][0] += flipper_length
            sums[species][1] += body_mass
            sums[species][2] += culmen_length
            sums[species][3] += culmen_depth
            counts[species] += 1
        print("Step 5: Iterate over data - Success")
    except Exception as e:
        print(f"Step 5: Iterate over data - Error: {e}")
        return

    try:
        # Calculate averages
        averages = {}
        for species in sums:
            if counts[species] > 0:
                averages[species] = [
                    sums[species][0] / counts[species],
                    sums[species][1] / counts[species],
                    sums[species][2] / counts[species],
                    sums[species][3] / counts[species]
                ]
        print("Step 6: Calculate averages - Success")
    except Exception as e:
        print(f"Step 6: Calculate averages - Error: {e}")
        return

    try:
        # Write the results to a new CSV file
        with open(output_csv, 'w') as file:
            file.write('Species,Flipper Length (mm),Body Mass (g),Culmen Length (mm),Culmen Depth (mm)\n')
            for species, avg in averages.items():
                file.write(f'{species},{avg[0]},{avg[1]},{avg[2]},{avg[3]}\n')
        print("Step 7: Write to CSV file - Success")
    except Exception as e:
        print(f"Step 7: Write to CSV file - Error: {e}")

# Example usage
calculate_penguin_averages('palmerpenguins_litter.csv', 'penguin_averages.csv')   