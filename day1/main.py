import re


def find_first_digit(line) -> int:
    match = re.search(r'(\d)', line)
    return int(match.group(0)) if match else None


with open('day1/input.txt', 'r') as file:
    content = file.read()

total = sum([find_first_digit(line) * 10 + find_first_digit(line[::-1])
             for line in content.splitlines()])

print(total)
