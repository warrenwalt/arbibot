import itertools

# Initial data structure with bookmaker names
bookmaker_odds_example_for_1x2 = [
    [("Betika", 1.20), ("Betika", 2.44), ("Betika", 6.00)],  # Betika
    [("SportPesa", 1.50), ("SportPesa", 1.90), ("SportPesa", 10.03)],  # SportPesa
    # [("Bet99", 1.20), ("Bet99", 2.44), ("Bet99", 6.00)],  # Bet99
]

# Transpose the matrix to group odds by outcomes
transposed_odds = list(zip(*bookmaker_odds_example_for_1x2))

# Generate all possible combinations of odds for each outcome
cartesian_product = list(itertools.product(*transposed_odds))

[
    (('Betika', 1.2), ('Betika', 2.44), ('Betika', 6.0)),
    (('Betika', 1.2), ('Betika', 2.44), ('SportPesa', 10.03)),
    (('Betika', 1.2), ('SportPesa', 1.9), ('Betika', 6.0)),
    (('Betika', 1.2), ('SportPesa', 1.9), ('SportPesa', 10.03)),
    (('SportPesa', 1.5), ('Betika', 2.44), ('Betika', 6.0)),
    (('SportPesa', 1.5), ('Betika', 2.44), ('SportPesa', 10.03)),
    (('SportPesa', 1.5), ('SportPesa', 1.9), ('Betika', 6.0)),
    (('SportPesa', 1.5), ('SportPesa', 1.9), ('SportPesa', 10.03))
]

# Function to extract and print combinations with bookmakers


def extract_combinations_with_bookmakers(cartesian_product):
    combinations_with_bookmakers = []
    for combination in cartesian_product:
        bookmakers = [odd[0] for odd in combination]
        odds = [odd[1] for odd in combination]
        combinations_with_bookmakers.append((bookmakers, odds))
    return combinations_with_bookmakers


[
    (['Betika', 'Betika', 'Betika'], [1.2, 2.44, 6.0]),
    (['Betika', 'Betika', 'SportPesa'], [1.2, 2.44, 10.03]),
    (['Betika', 'SportPesa', 'Betika'], [1.2, 1.9, 6.0]),
    (['Betika', 'SportPesa', 'SportPesa'], [1.2, 1.9, 10.03]),
    (['SportPesa', 'Betika', 'Betika'], [1.5, 2.44, 6.0]),
    (['SportPesa', 'Betika', 'SportPesa'], [1.5, 2.44, 10.03]),
    (['SportPesa', 'SportPesa', 'Betika'], [1.5, 1.9, 6.0]),
    (['SportPesa', 'SportPesa', 'SportPesa'], [1.5, 1.9, 10.03])
]


# Extract and print the valid combinations
valid_combinations_with_bookmakers = extract_combinations_with_bookmakers(
    cartesian_product)
for combination in valid_combinations_with_bookmakers:
    print("Bookmakers:", combination[0], "Odds:", combination[1], "\n")
