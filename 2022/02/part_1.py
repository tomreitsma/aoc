from entities import Entity

from typing import Tuple, List


def parse_input(input):
    moves = []

    for line in input:
        column_a, column_b = line.strip().split(" ")

        moves.append((Entity.factory(column_a), Entity.factory(column_b),))

    return moves


def compute_strategy(moves: List[Tuple[Entity, Entity]]):
    scores = []
    for opponent_move, player_move in moves:
        print(f"Comparing {opponent_move} with {player_move}")

    return scores


if __name__ == "__main__":
    moves = parse_input(open("input.txt").readlines())

    results = compute_strategy(moves)

    p1 = sum(results)
    assert p1 == 10994


