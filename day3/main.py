import re


def find_overlapping(line, start_index, end_index, regex):
    overlapping = []

    for match in re.finditer(regex, line):
        digit_start, digit_end = match.span()

        if digit_start < end_index and digit_end > start_index:
            overlapping.append(match.group())

    return overlapping


def check_engine_part(lines, line_idx, start_index, end_index):
    regex = r'[^0-9.]'
    # Check same line
    if find_overlapping(lines[line_idx], start_index-1, end_index+1, regex):
        return True

    # Check previous line
    if line_idx >= 1 and find_overlapping(lines[line_idx-1], start_index-1, end_index+1, regex):
        return True

    # Check next line
    if line_idx < len(lines) - 1 and find_overlapping(lines[line_idx+1], start_index-1, end_index+1, regex):
        return True

    return False


def check_gear(lines, line_idx, idx):
    regex = r'\d+'
    adjacent_digits = []

    # Check same line
    digits_same_line = find_overlapping(lines[line_idx], idx-1, idx+2, regex)
    if digits_same_line:
        adjacent_digits.extend(digits_same_line)

    # Check previous line
    if line_idx >= 1:
        digits_previous_line = find_overlapping(lines[line_idx-1], idx-1, idx+2, regex)
        if digits_previous_line:
            adjacent_digits.extend(digits_previous_line)

    # Check next line
    if line_idx < len(lines):
        digits_next_line = find_overlapping(lines[line_idx+1], idx-1, idx+2, regex)
        if digits_next_line:
            adjacent_digits.extend(digits_next_line)

    if len(adjacent_digits) == 2:
        return True, int(adjacent_digits[0]), int(adjacent_digits[1])

    return False, None, None


with open('day3/input.txt', 'r') as file:
    lines = file.read().splitlines()

engine_parts = [
    [int(match.group()) for match in re.finditer(r'\d+', line)
        if check_engine_part(lines, i, match.start(), match.end())]
    for i, line in enumerate(lines)
]

total = sum(int(part) for line_parts in engine_parts for part in line_parts)
print(f"Part 1 total: {total}")

gear_digits = []
for i, line in enumerate(lines):
    for match in re.finditer(r'\*', line):
        is_gear, digit1, digit2 = check_gear(lines, i, match.start())
        if is_gear:
            gear_digits.append((digit1, digit2))

total = sum(digit1 * digit2 for digit1, digit2 in gear_digits)
print(f"Part 2 total: {total}")
