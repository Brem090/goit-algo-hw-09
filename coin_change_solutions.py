import time

def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count
            if amount == 0:
                break
    return result

def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    min_coins = [0] + [float('inf')] * amount
    last_coin = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                last_coin[i] = coin

    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = last_coin[current_amount]
        result[coin] = result.get(coin, 0) + 1
        current_amount -= coin

    return result

def form_result(result, title):
    formatted_output = f"{title}:\n"
    for coin, count in sorted(result.items(), reverse=True):
        formatted_output += f"Номінал {coin} копійок: {count} монет(и)\n"
    return formatted_output

def form_execution_time(function, *args):
    start_time = time.time()
    function(*args)
    end_time = time.time()
    execution_time_ms = (end_time - start_time) * 1000
    return execution_time_ms

small_amount = 113

greedy_result_example = find_coins_greedy(small_amount)
dp_result_example = find_min_coins(small_amount)

print(form_result(greedy_result_example, "Результат Жадібного Алгоритму для малої суми"))
print(form_result(dp_result_example, "Результат Динамічного Програмування для малої суми"))

greedy_time_example = form_execution_time(find_coins_greedy, small_amount)
dp_time_example = form_execution_time(find_min_coins, small_amount)

print(f"Час виконання Жадібного Алгоритму для малої суми: {greedy_time_example:.4f} мс")
print(f"Час виконання Динамічного Програмування для малої суми: {dp_time_example:.4f} мс")

print("-" * 70)

large_amount = 123456

greedy_result_large = find_coins_greedy(large_amount)
dp_result_large = find_min_coins(large_amount)

print(form_result(greedy_result_large, "Результат Жадібного Алгоритму для великої суми"))
print(form_result(dp_result_large, "Результат Динамічного Програмування для великої суми"))

greedy_time_large = form_execution_time(find_coins_greedy, large_amount)
dp_time_large = form_execution_time(find_min_coins, large_amount)

print(f"Час виконання Жадібного Алгоритму для великої суми: {greedy_time_large:.4f} мс")
print(f"Час виконання Динамічного Програмування для великої суми: {dp_time_large:.4f} мс")

