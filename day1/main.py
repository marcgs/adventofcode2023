import re


word_to_num = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def convert(part):
    return word_to_num.get(part) if part in word_to_num else int(part)


def calculate(line) -> int:

    nums = 'one|two|three|four|five|six|seven|eight|nine'
    matches = re.findall(f'(\\d|{nums})', line)
    first = convert(matches[0])

    matches = re.findall(f'(\\d|{nums[::-1]})', line[::-1])
    last = convert(matches[0][::-1])
    return first * 10 + last


with open('day1/input.txt', 'r') as file:
    content = file.read()

results = [calculate(line) for line in content.splitlines()]
total = sum(results)

print(total)
