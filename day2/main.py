from dataclasses import dataclass
import re


@dataclass
class Game:
    id: int
    cubes: dict[str, int]


def is_valid(game: Game) -> bool:
    result = game.cubes.get('red', 0) <= 12 and \
            game.cubes.get('green', 0) <= 13 and \
            game.cubes.get('blue', 0) <= 14
    return result


def parse_game(line) -> Game:
    match = re.search(r'Game (\d+): (.*)', line)
    id = int(match.group(1))
    cubes = {}
    for cube_set in match.group(2).split(', '):
        match = re.search(r'(\d+) (\w+)', cube_set)
        count = int(match.group(1))
        color = match.group(2)
        cubes[color] = max(cubes.get(color, 0), count)

    return Game(id, cubes)


def parse_games(content) -> list[Game]:
    new_content = content.replace(';', ',')
    games: list[Game] = []
    for line in new_content.splitlines():
        game = parse_game(line)
        games.append(game)
    return games


with open('day2/input.txt', 'r') as file:
    content = file.read()
    games = parse_games(content)
    valid_games = [game.id for game in games if is_valid(game)]
    print(f"valid games = {valid_games}")
    score = sum(valid_games)
    print(f"score = {score}")
