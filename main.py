print()

print("Apple: $1.00")
num_apples = int(input("How many apples to buy? "))
cost_apples = 1 * num_apples
print(f"The apples cost ${cost_apples:.2f}.\n")

print("Orange: $1.50")
num_oranges = int(input("How many oranges to buy? "))
cost_oranges = 1.5 * num_oranges
print(f"The oranges cost ${cost_oranges:.2f}.\n")

print("Candy bar: $2.00")
num_candy_bars = int(input("How many candy bars to buy? "))
cost_candy_bars = 2 * num_candy_bars
print(f"The candy bars cost ${cost_candy_bars:.2f}.\n")

total_cost = cost_apples + cost_oranges + cost_candy_bars
print(f"The total cost is ${total_cost:.2f}.")
