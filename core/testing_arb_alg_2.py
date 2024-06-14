import itertools
import time

# Input odds from different bookmakers
bookmaker_odds = bookmaker_odds = [
    [1.20, 2.44, 6.00],  # Betika
    [1.5, 1.9, 10.03],   # SportPesa
    [1.0, 2.0, 3.0],     # Bet9ja
    [3.22, 3.98, 11.00],  # Mozzart
    [3.54, 4.21, 13.74],  # Bookmaker 5
    [2.78, 1.13, 11.65],  # Bookmaker 6
    [3.43, 2.59, 8.56],  # Bookmaker 7
    [1.88, 4.23, 9.64],  # Bookmaker 8
    [2.46, 4.72, 14.37],  # Bookmaker 9
    [3.03, 1.91, 9.57],  # Bookmaker 10
    [3.79, 1.78, 8.59],  # Bookmaker 11
    [1.52, 1.68, 7.59],  # Bookmaker 12
    [1.44, 2.94, 11.69],  # Bookmaker 13
    [2.32, 2.01, 8.93],  # Bookmaker 14
    [2.14, 4.41, 13.35],  # Bookmaker 15
    [1.65, 1.29, 11.43],  # Bookmaker 16
    [2.95, 3.81, 10.05],  # Bookmaker 17
    [1.06, 2.93, 5.99],  # Bookmaker 18
    [3.73, 4.39, 12.43],  # Bookmaker 19
    [2.96, 2.75, 6.99],  # Bookmaker 20
    [1.02, 2.69, 6.84],  # Bookmaker 21
    [3.54, 2.63, 8.06],  # Bookmaker 22
    [2.16, 3.58, 12.86],  # Bookmaker 23
    [3.94, 2.06, 9.21],  # Bookmaker 24
    [2.27, 2.39, 11.37],  # Bookmaker 25
    [1.98, 4.82, 9.56],  # Bookmaker 26
    [1.59, 2.83, 6.63],  # Bookmaker 27
    [3.49, 4.54, 6.77],  # Bookmaker 28
    [2.89, 4.56, 6.34],  # Bookmaker 29
    [2.26, 1.94, 7.93],  # Bookmaker 30
    [2.27, 1.66, 5.64],  # Bookmaker 31
    [3.41, 3.58, 14.74],  # Bookmaker 32
    [1.32, 1.13, 14.14],  # Bookmaker 33
    [1.07, 4.64, 6.43],  # Bookmaker 34
    [3.84, 4.96, 10.91],  # Bookmaker 35
    [3.17, 2.27, 12.31],  # Bookmaker 36
    [1.66, 3.11, 6.05],  # Bookmaker 37
    [3.64, 4.24, 12.19],  # Bookmaker 38
    [1.56, 4.38, 10.59],  # Bookmaker 39
    [2.99, 2.27, 10.82],  # Bookmaker 40
    [1.08, 4.66, 14.46],  # Bookmaker 41
    [2.58, 4.55, 11.22],  # Bookmaker 42
    [1.39, 1.36, 5.84],  # Bookmaker 43
    [1.91, 1.76, 11.48],  # Bookmaker 44
    [1.88, 1.51, 8.18],  # Bookmaker 45
    [3.69, 4.27, 7.35],  # Bookmaker 46
    [3.38, 1.75, 8.31],  # Bookmaker 47
    [2.72, 2.23, 9.64],  # Bookmaker 48
    [3.74, 3.68, 7.35],  # Bookmaker 49
    [1.19, 1.89, 5.61],  # Bookmaker 50
    [3.29, 1.82, 13.73],  # Bookmaker 51
    [2.16, 4.37, 6.93],  # Bookmaker 52
    [1.36, 2.12, 11.34],  # Bookmaker 53
    [2.31, 2.99, 10.41],  # Bookmaker 54
]

# Transpose the matrix using zip and unpacking
[
    [1.2, 1.5],
    [2.44, 1.9],
    [6.0, 10.03]
]

[(1.2, 2.44, 6.0), (1.2, 2.44, 10.03), (1.2, 2.44, 3.0),  # VALID!
 (1.2, 1.9, 6.0), (1.2, 1.9, 10.03), (1.2, 1.9, 3.0),  # VALID!
 (1.2, 2.0, 6.0), (1.2, 2.0, 10.03), (1.2, 2.0, 3.0),  # VALID!
 (1.5, 2.44, 6.0), (1.5, 2.44, 10.03), (1.5, 2.44, 3.0),  # VALID!
 (1.5, 1.9, 6.0), (1.5, 1.9, 10.03), (1.5, 1.9, 3.0),  # VALID!
 (1.5, 2.0, 6.0), (1.5, 2.0, 10.03), (1.5, 2.0, 3.0),  # VALID!
 (1.0, 2.44, 6.0), (1.0, 2.44, 10.03), (1.0, 2.44, 3.0),  # VALID!
 (1.0, 1.9, 6.0), (1.0, 1.9, 10.03), (1.0, 1.9, 3.0),  # VALID!
 (1.0, 2.0, 6.0), (1.0, 2.0, 10.03), (1.0, 2.0, 3.0)  # VALID!
 ]

[(1.2, 2.44, 6.0), (1.2, 2.44, 10.03), (1.2, 1.9, 6.0), (1.2, 1.9, 10.03),
 (1.5, 2.44, 6.0), (1.5, 2.44, 10.03), (1.5, 1.9, 6.0), (1.5, 1.9, 10.03)]

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
