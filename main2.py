import re

def generator_numbers(text):
    numbers = re.findall(r'\b\d+(?:\.\d+)?\b', text)
    for number in numbers:
        yield float(number)  


def sum_profit(text):
    return sum(generator_numbers(text))

text = "У нас є прибуток 100.50 і витрати 50.25, а також додатковий дохід 200"
total_profit = sum_profit(text)
print(f"Загальний прибуток: {total_profit}")
