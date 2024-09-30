# Function to parse the species and body mass from the CSV line
def parse_species_and_body_mass(line):
    columns = line.strip().split(',')
    try:
        species = columns[2]
        body_mass = columns[13]
    except IndexError:
        # Handle the case where the line does not have enough columns
        return None, None
    return species, body_mass

# Read the CSV file and find the species with the largest body mass
try:
    with open(r'C:\Users\trash\OneDrive\Data science\palmerpenguins_litter.csv', 'r') as file:
        # Skip the header line
        next(file)
        
        # Initialize variables to store the species with the largest body mass
        max_body_mass = 0
        species_with_max_body_mass = None
        
        for line in file:
            species, body_mass = parse_species_and_body_mass(line)
            
            # Check if species and body mass are valid
            if species is None or body_mass is None:
                continue
            
            # Check if body mass is not empty and convert it to an integer
            if body_mass:
                try:
                    body_mass = int(body_mass)
                except ValueError:
                    # Handle the case where body mass is not a valid integer
                    continue
                
                if body_mass > max_body_mass:
                    max_body_mass = body_mass
                    species_with_max_body_mass = species

    # Print the species with the largest body mass
    print("Species with the largest Body Mass (g):", species_with_max_body_mass)
    print("Largest Body Mass (g):", max_body_mass)

except FileNotFoundError:
    print("The file was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")