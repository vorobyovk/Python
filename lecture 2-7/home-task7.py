import random
import matplotlib.pyplot as plt

def stock_price_at_time(t=3):
    price = 0
    for _ in range(t):
        change = random.choice([2, -1])  # Randomly choose +2 or -1
        price += change
    return price

def simulate_n_times(n: int, t: int):
    final_prices = []
    for _ in range(num_simulations):
        final_price = stock_price_at_time(t)
        final_prices.append(final_price)
    average_price = sum(final_prices) / n
    return average_price, final_prices    

def plot_histogram(final_prices, num_simulations):
    plt.hist(final_prices, bins=range(min(final_prices) - 1, max(final_prices) + 2), edgecolor='black')
    plt.title(f'Stock Price Distribution ({num_simulations} Simulations)')
    plt.xlabel('Final Stock Price')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    num_simulations_list = [10, 100, 1000, 10000]
    for num_simulations in num_simulations_list:
        avg_price, all_prices = simulate_n_times(num_simulations, 3)
        print(f"\n--- {num_simulations} Simulations ---")
        print(f"Average final stock price: {avg_price}")
        plot_histogram(all_prices, num_simulations)
        