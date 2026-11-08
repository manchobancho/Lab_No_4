def calculate_evarage(numbers):
    s = 0
    for number in numbers:
       s = s + number
    evarage = s / len(numbers)
    return "evarage: ", evarage
def find_min(numbers):
    minimum = numbers[0]
    for number in numbers:
        if minimum > number:
            minimum = number
    return "minimum: ", minimum
def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return "maximum: ", maximum