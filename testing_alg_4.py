def calculate_implied_probabilities(odds):
    return [1 / odd for odd in odds]


def detect_arbitrage(odds_combination, total_investment=100):
    book_makers = odds_combination[0]
    odds = odds_combination[1]
    implied_probabilities = calculate_implied_probabilities(odds)
    sum_implied_probabilities = sum(implied_probabilities)

    if sum_implied_probabilities < 1:
        stakes = [total_investment * implied_prob / sum_implied_probabilities
                  for implied_prob in implied_probabilities]
        returns = [stake * odd for stake, odd in zip(stakes, odds)]
        profit = min(returns) - total_investment
        return True, stakes, profit, book_makers
    else:
        return False, [], 0, book_makers


odds_combinations = [
    (['Betika', 'Betika', 'Betika'], [1.2, 2.44, 6.0]),
    (['Betika', 'Betika', 'SportPesa'], [1.2, 2.44, 10.03]),
    (['Betika', 'SportPesa', 'Betika'], [1.2, 1.9, 6.0]),
    (['Betika', 'SportPesa', 'SportPesa'], [1.2, 1.9, 10.03]),
    (['SportPesa', 'Betika', 'Betika'], [1.5, 2.44, 6.0]),
    (['SportPesa', 'Betika', 'SportPesa'], [1.5, 2.44, 10.03]),
    (['SportPesa', 'SportPesa', 'Betika'], [1.5, 1.9, 6.0]),
    (['SportPesa', 'SportPesa', 'SportPesa'], [1.5, 1.9, 10.03])
]


for combination in odds_combinations:
    is_arbitrage, stakes, profit, book_makers = detect_arbitrage(combination)
    if is_arbitrage:
        print(f"Arbitrage opportunity detected with odds {combination}")
        print(f"Stakes to place: {stakes}")
        print(f"Guaranteed profit: ${profit:.2f}")
