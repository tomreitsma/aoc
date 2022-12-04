from constants import ROCK, PAPER, SCISSORS, SCORES, DRAW, LOSS, WIN


class Entity:
    name = None
    beats = None

    @staticmethod
    def factory(character_input: str):
        try:
            return {
                "A": Rock(),
                "B": Paper(),
                "C": Scissors(),

                "X": Rock(),
                "Y": Paper(),
                "Z": Scissors()
            }[character_input]
        except IndexError:
            raise Exception("Invalid character")

    @property
    def value(self):
        return SCORES[self.name]

    def get_move_for_desired_outcome(self, outcome):
        for e in (Rock(), Paper(), Scissors()):
            if e.get_result(self) == outcome:
                return e

    def get_result(self, other):
        if self.name == other.name:
            return DRAW
        elif self.beats == other.name:
            return WIN
        elif other.beats == self.name:
            return LOSS

    def get_score(self, result):
        print(f"Getting score for result: {result}")
        score = 0
        if result == DRAW:
            score = SCORES[DRAW]
        elif result == LOSS:
            score = SCORES[LOSS]
        elif result == WIN:
            score = SCORES[WIN]

        print(f"{self.value} {score}")
        return self.value + score

    def __str__(self):
        return self.name


class Rock(Entity):
    name = ROCK
    beats = SCISSORS


class Scissors(Entity):
    name = SCISSORS
    beats = PAPER


class Paper(Entity):
    name = PAPER
    beats = ROCK
