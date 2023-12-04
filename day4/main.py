from dataclasses import dataclass
import re


@dataclass
class Card:
    id: str
    winning_nums: list[int]
    my_nums: list[int] 


with open('day4/input.txt', 'r') as file:
    lines = [line.strip() for line in file]


cards = []
for line in lines:
    match = re.search(r'Card\s+(\d+): (.*)$', line)
    id = match.group(1)
    nums = match.group(2)

    split = nums.split('|')
    winning_nums = re.findall(r'\d+', split[0])
    my_nums = re.findall(r'\d+', split[1])

    cards.append(Card(id, winning_nums, my_nums))

amount_wins = [sum(1 for num in card.my_nums if num in card.winning_nums) for card in cards]

scores = [2**(amount-1) for amount in amount_wins if amount > 0]

print(sum(scores))