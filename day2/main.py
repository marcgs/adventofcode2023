from dataclasses import dataclass
import re


@dataclass
class Game:
    id: int
    cube_sets: list[dict[str, int]]


def is_valid(game: Game) -> bool:
    return not any(
        cube_set.get('red', 0) > 12 or
        cube_set.get('green', 0) > 13 or
        cube_set.get('blue', 0) > 14
        for cube_set in game.cube_sets
    )


def parse_game(line) -> Game:
    match = re.search(r'Game (\d+): (.*)', line)
    game_id = int(match.group(1))
    game_data = match.group(2).split('; ')
    cube_sets = [
        {color: int(count) for count, color
            in re.findall(r'(\d+) (\w+)', cube_set)}
        for cube_set in game_data
    ]
    return Game(game_id, cube_sets)


def parse_games(content) -> list[Game]:
    return [parse_game(line) for line in content.splitlines()]


with open('day2/input.txt', 'r') as file:
    content = file.read()
    games = parse_games(content)
    valid_games = [game.id for game in games if is_valid(game)]
    print(f"valid games = {valid_games}")
    score = sum(valid_games)
    print(f"score = {score}")
