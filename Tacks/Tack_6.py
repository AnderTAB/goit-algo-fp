def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    selected_items = []
    remaining_budget = budget

    for item_name, item_info in sorted_items:
        if item_info["cost"] <= remaining_budget:
            selected_items.append(item_name)
            remaining_budget -= item_info["cost"]

    return selected_items

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            cost_i = items[list(items.keys())[i - 1]]["cost"]
            calories_i = items[list(items.keys())[i - 1]]["calories"]
            if cost_i <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost_i] + calories_i)
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    i, w = n, budget
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(list(items.keys())[i - 1])
            w -= items[list(items.keys())[i - 1]]["cost"]
        i -= 1

    return selected_items

if __name__ == "__main__":
    items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
    budget_limit = 60
    selected_greedy_algorithm = greedy_algorithm(items, budget_limit)
    print(f"Жадібний алгоритм:")
    print(f"Найкраще меню за доступні грощі {budget_limit}: {selected_greedy_algorithm}")
    selected_dynamic_programming = dynamic_programming(items, budget_limit)
    print(f"Алгоритм динамічного програмування:")
    print(f"Найкраще меню за доступні грощі {budget_limit}: {selected_dynamic_programming}")