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
]

# Transpose the matrix using zip and unpacking
[
    [1.2, 1.5],
    [2.44, 1.9],
    [6.0, 10.03]
]

# Generate all possible combinations of odds for each outcome
cartesian_product = [
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
# print(f'Execution time: {execution_time} milliseconds')
# print(f'total odd combinations✅✅::> {len(odds_combinations)}'.upper())
# print('SIZE OF ALL POSSIBLE COMBINATIONS:',
#       sys.getsizeof(odds_combinations)/1000, 'KB')


"""FINDING ARBITRAGE OPPORTUNITIES"""


def calculate_implied_probabilities(odds):
    return [1 / odd for odd in odds]


def detect_arbitrage(odds_combination, total_investment=100):
    implied_probabilities = calculate_implied_probabilities(odds_combination)
    sum_implied_probabilities = sum(implied_probabilities)

    if sum_implied_probabilities < 1:
        stakes = [total_investment * implied_prob /
                  sum_implied_probabilities for implied_prob in implied_probabilities]
        returns = [stake * odd for stake, odd in zip(stakes, odds_combination)]
        profit = min(returns) - total_investment
        return True, stakes, profit
    else:
        return False, [], 0


# print(f'odds combinations🙏 {odds_combinations}')
for combination in odds_combinations:
    is_arbitrage, stakes, profit = detect_arbitrage(combination)
    if is_arbitrage:
        print(f"Arbitrage opportunity detected with odds {combination}")
        print(f"Stakes to place: {stakes}")
        print(f"Guaranteed profit: ${profit:.2f}")
