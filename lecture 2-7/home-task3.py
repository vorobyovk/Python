import itertools

def dice_probabilities():
    dice_values = [1, 2, 3, 4, 5, 6]
    all_outcomes = list(itertools.product(dice_values, dice_values, dice_values))  # All possible combinations
    count_11 = 0
    count_12 = 0
    outcomes_11 = []
    outcomes_12 = []
    for outcome in all_outcomes:
        if sum(outcome) == 11:
            count_11 += 1
            outcomes_11.append(outcome)
        elif sum(outcome) == 12:
            count_12 += 1
            outcomes_12.append(outcome)
    total_outcomes = len(all_outcomes)
    probability_11 = count_11 / total_outcomes
    probability_12 = count_12 / total_outcomes
    return probability_11, probability_12, outcomes_11, outcomes_12

if __name__ == "__main__":
    prob_11, prob_12, outcomes_11, outcomes_12 = dice_probabilities()
    print(f"Probability of getting a sum of 11: {prob_11}")
    print(f"Probability of getting a sum of 12: {prob_12}")
    print(f"Outcomes summing to 11: {outcomes_11}")
    print(f"Outcomes summing to 12: {outcomes_12}")
    if prob_11 > prob_12:
        print("It's more probable to get a sum of 11.")
    elif prob_12 > prob_11:
        print("It's more probable to get a sum of 12.")
    else:
        print("The probabilities are equal.")
        