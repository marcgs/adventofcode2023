from dataclasses import dataclass
import re


@dataclass
class Card:
    id: str
    winning_nums: list[int]
    my_nums: list[int]
    wins: int
    amount: int


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
    wins = sum(1 for num in my_nums if num in winning_nums)

    cards.append(Card(id, winning_nums, my_nums, wins, amount=1))

score = sum([2**(card.wins-1) for card in cards if card.wins > 0])
print(f"Part1 score: {score}")


for i, card in enumerate(cards):
    for j in range(1, card.wins + 1):
        if (i + j < len(cards)):
            cards[i + j].amount += cards[i].amount

score = sum((card.amount for card in cards))
print(f"Part2 score: {score}")
