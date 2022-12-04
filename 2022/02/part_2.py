from typing import Tuple, List

from constants import SCORES, DRAW, LOSS, WIN, OUTCOME_MAPPINGS
from entities import Entity


def parse_input(input):
    moves = []

    for line in input:
        opponent_move, desired_outcome = line.strip().split(" ")

        moves.append((Entity.factory(opponent_move), OUTCOME_MAPPINGS[desired_outcome],))

    return moves


def compute_strategy(moves: List[Tuple[Entity, str]]):
    scores = []
    for opponent_move, desired_outcome in moves:
        print(f"{opponent_move}. Desired outcome: {desired_outcome}")

        player_move = opponent_move.get_move_for_desired_outcome(desired_outcome)
        print(f"Got player move: {player_move}")
        result = player_move.get_result(opponent_move)

        scores.append(player_move.get_score(result))
        print("")

    print(scores)

    return scores


if __name__ == "__main__":
    moves = parse_input(open("input.txt").readlines())

    results = compute_strategy(moves)

    p1 = sum(results)
    print(p1)
