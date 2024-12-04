import re
from typing import Callable

def generator_numbers(text):
    numbers = re.findall(r'\b\d+(?:\.\d+)?\b', text)
    for number in numbers:
        yield float(number)  

def sum_profit(text: str, func: Callable[[str], float]) -> float:
    return sum(func(text))

text = "The profits are 167, 236 and 351."
total_profit = sum_profit(text, generator_numbers)
print(total_profit)