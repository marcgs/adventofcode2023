import re


def find_first_digit(line):
    match = re.search(r'(\d)', line)
    return match.group(0) if match else None


# Open and read the file
with open('input.txt', 'r') as file:
    content = file.read()

# File is automatically closed after the with block
sum = 0
for line in content.splitlines():
    first_digit = find_first_digit(line)
    last_digit = find_first_digit(line[::-1])
    num = int(first_digit) * 10 + int(last_digit)
    sum += num

print(sum)
