import random
import matplotlib.pyplot as plt

def simulate_stock_price(num_periods=3):
    price = 0
    for _ in range(num_periods):
        change = random.choice([2, -1])  # Randomly choose +2 or -1
        price += change
    return price

def run_simulations(num_simulations, num_periods=3):   
    final_prices = []
    for _ in range(num_simulations):
        final_price = simulate_stock_price(num_periods)
        final_prices.append(final_price)

    average_price = sum(final_prices) / num_simulations
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
        avg_price, all_prices = run_simulations(num_simulations)
        print(f"\n--- {num_simulations} Simulations ---")
        print(f"Average final stock price: {avg_price}")
        plot_histogram(all_prices, num_simulations)
        