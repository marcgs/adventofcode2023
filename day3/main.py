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


with open('day3/input.txt', 'r') as file:
    lines = file.read().splitlines()

engine_parts = [
    [int(match.group()) for match in re.finditer(r'\d+', line)
        if is_engine_part(lines, i, match.start(), match.end())]
    for i, line in enumerate(lines)
]

print(engine_parts)

total = sum(int(part) for line_parts in engine_parts for part in line_parts)
print(f"total: {total}")
