import csv

class Penguin:
    def __init__(self, study_name, sample_number, species, region, island, stage, individual_id, clutch_completion, date_egg, culmen_length, culmen_depth, flipper_length, body_mass, sex, delta_15_n, delta_13_c, comments):
        self.study_name = study_name
        self.sample_number = sample_number
        self.species = species
        self.region = region
        self.island = island
        self.stage = stage
        self.individual_id = individual_id
        self.clutch_completion = clutch_completion
        self.date_egg = date_egg
        self.culmen_length = culmen_length
        self.culmen_depth = culmen_depth
        self.flipper_length = flipper_length
        self.body_mass = body_mass
        self.sex = sex
        self.delta_15_n = delta_15_n
        self.delta_13_c = delta_13_c
        self.comments = comments

def create_penguins_from_csv(file_path):
    penguins = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Remove extra comma in "Clutch Completion" field
            row['Clutch Completion'] = row['Clutch Completion'].replace(',', '')
            penguin = Penguin(
                row['studyName'],
                row['Sample Number'],
                row['Species'],
                row['Region'],
                row['Island'],
                row['Stage'],
                row['Individual ID'],
                row['Clutch Completion'],
                row['Date Egg'],
                row['Culmen Length (mm)'],
                row['Culmen Depth (mm)'],
                row['Flipper Length (mm)'],
                row['Body Mass (g)'],
                row['Sex'],
                row['Delta 15 N (o/oo)'],
                row['Delta 13 C (o/oo)'],
                row['Comments']
            )
            penguins.append(penguin)
    return penguins

# Example usage
file_path = 'palmerpenguins_litter.csv'
penguins = create_penguins_from_csv(file_path)

# Print the first penguin object to verify
print(vars(penguins[5])) 