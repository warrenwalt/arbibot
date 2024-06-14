import itertools
import time


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


# Input odds from different bookmakers
bookmaker_odds = [
    [1.20, 2.44, 6.00],  # Betika
    [1.5, 1.9, 10.03],    # SportPesa
]

# Generate all possible combinations of odds for each outcome

start_time = time.time()

odds_combinations = list(itertools.product(*bookmaker_odds))

end_time = time.time()
execution_time = (end_time - start_time) * 1000
# print('odds combinations🙏', odds_combinations)
print(f'Execution time: {execution_time} milliseconds')
print(len(odds_combinations))

# Check each combination for arbitrage opportunities
# for combination in odds_combinations:
#     is_arbitrage, stakes, profit = detect_arbitrage(combination)
#     if is_arbitrage:
#         print(f"Arbitrage opportunity detected with odds {combination}")
#         print(f"Stakes to place: {stakes}")
#         print(f"Guaranteed profit: ${profit:.2f}")
# else:
#     print(f"No arbitrage opportunity with odds {combination}")
