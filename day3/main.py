import re


def has_special_char(line, index_start, index_end):
    index_start = max(0, index_start)
    index_end = min(len(line), index_end)
    return bool(re.search(r'[^0-9.]', line[index_start:index_end]))


def is_engine_part(lines, line_idx, part_start_idx, part_end_idx):
    # Check same line
    if has_special_char(lines[line_idx], part_start_idx-1, part_end_idx+1):
        return True

    # Check previous line
    if line_idx >= 1 and has_special_char(lines[line_idx-1], part_start_idx-1, part_end_idx+1):
        return True

    # Check next line
    if line_idx < len(lines) - 1 and has_special_char(lines[line_idx+1], part_start_idx-1, part_end_idx+1):
        return True

    return False


def find_overlapping(line, start_index, end_index, regex=r'\d+'):
    overlapping_digits = []

    for match in re.finditer(regex, line):
        digit_start, digit_end = match.span()

        if digit_start <= end_index and digit_end > start_index:
            overlapping_digits.append(match.group())

    return overlapping_digits


def check_gear(lines, line_idx, idx):
    adjacent_digits = []

    # Check same line
    digits_same_line = find_overlapping(lines[line_idx], idx-1, idx+1)
    if digits_same_line:
        adjacent_digits.extend(digits_same_line)

    # Check previous line
    if line_idx >= 1:
        digits_previous_line = find_overlapping(lines[line_idx-1], idx-1, idx+1)
        if digits_previous_line:
            adjacent_digits.extend(digits_previous_line)

    # Check next line
    if line_idx < len(lines):
        digits_next_line = find_overlapping(lines[line_idx+1], idx-1, idx+1)
        if digits_next_line:
            adjacent_digits.extend(digits_next_line)

    if len(adjacent_digits) == 2:
        return True, int(adjacent_digits[0]), int(adjacent_digits[1])

    return False, None, None


with open('day3/input.txt', 'r') as file:
    lines = file.read().splitlines()

engine_parts = [
    [int(match.group()) for match in re.finditer(r'\d+', line)
        if is_engine_part(lines, i, match.start(), match.end())]
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
     
total = sum((digits[0]*digits[1] for digits in gear_digits))
print(f"Part 2 total: {total}")
