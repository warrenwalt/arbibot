import itertools
import time
import random
import sys

# Input odds from different bookmakers
# Function to generate random odds

bookmaker_odds = []


bookmaker_odds_example_for_1x2 = [
    [1.20, 2.44, 6.00],  # Betika
    [1.5, 1.9, 10.03],   # SportPesa
    [1.0, 2.0, 3.0],     # Bet9ja
    [3.22, 3.98, 11.00],  # Mozzart
    [3.54, 4.21, 13.74],  # Bookmaker 5
    [2.78, 1.13, 11.65],  # Bookmaker 6
]

# Transpose the matrix using zip and unpacking
[
    [1.2, 1.5],
    [2.44, 1.9],
    [6.0, 10.03]
]

# Generate all possible combinations of odds for each outcome
[
    (1.2, 2.44, 6.0), (1.2, 2.44, 10.03), (1.2, 2.44, 3.0),  # VALID!
    (1.2, 1.9, 6.0), (1.2, 1.9, 10.03), (1.2, 1.9, 3.0),  # VALID!
    (1.2, 2.0, 6.0), (1.2, 2.0, 10.03), (1.2, 2.0, 3.0),  # VALID!
    (1.5, 2.44, 6.0), (1.5, 2.44, 10.03), (1.5, 2.44, 3.0),  # VALID!
    (1.5, 1.9, 6.0), (1.5, 1.9, 10.03), (1.5, 1.9, 3.0),  # VALID!
    (1.5, 2.0, 6.0), (1.5, 2.0, 10.03), (1.5, 2.0, 3.0),  # VALID!
    (1.0, 2.44, 6.0), (1.0, 2.44, 10.03), (1.0, 2.44, 3.0),  # VALID!
    (1.0, 1.9, 6.0), (1.0, 1.9, 10.03), (1.0, 1.9, 3.0),  # VALID!
    (1.0, 2.0, 6.0), (1.0, 2.0, 10.03), (1.0, 2.0, 3.0)  # VALID!
]

# [(1.2, 2.44, 6.0), (1.2, 2.44, 10.03), (1.2, 1.9, 6.0), (1.2, 1.9, 10.03),
#  (1.5, 2.44, 6.0), (1.5, 2.44, 10.03), (1.5, 1.9, 6.0), (1.5, 1.9, 10.03)]


def generate_random_odds():
    return [round(random.uniform(1.0, 4.0), 2),
            round(random.uniform(1.0, 5.0), 2),
            round(random.uniform(5.0, 15.0), 2)]


for _ in range(3):
    # 5_359_375 odd combinations for 175 bookmakers
    # in just under 1 second!
    bookmaker_odds.append(generate_random_odds())

# Transpose the matrix using zip and unpacking

start_time = time.time()
transposed_odds = list(zip(*bookmaker_odds))

# Convert tuples to lists (optional, depending on the desired output format)
transposed_odds = [list(row) for row in transposed_odds]


# Generate all possible combinations of odds for each outcome

odds_combinations = list(itertools.product(*transposed_odds))
end_time = time.time()
execution_time = (end_time - start_time) * 1000
print(f'Execution time: {execution_time} milliseconds')
print(f'total odd combinations✅✅::> {len(odds_combinations)}'.upper())
print('SIZE OF ALL POSSIBLE COMBINATIONS:',
      sys.getsizeof(odds_combinations)/1000, 'KB')
