def get_priority(item):
    o = ord(item)

    if 97 <= o <= 122:
        return o - 96
    elif 65 <= o <= 90:
        return o - 38


def get_overlaps(input):
    overlaps = []

    for line in input:
        half = len(line) // 2
        c1 = line[:half]
        c2 = line[half:]

        overlaps += list(set(c1) & set(c2))

    return overlaps


if __name__ == "__main__":
    test_input = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]

    assert get_priority("a") == 1
    assert get_priority("z") == 26
    assert get_priority("A") == 27
    assert get_priority("Z") == 52

    overlaps = get_overlaps(test_input)
    priorities = [get_priority(i) for i in overlaps]

    assert sum(priorities) == 157

    groups_overlaps = []

    step = 3
    for index in range(0, len(test_input), step):
        lines = test_input[index:index+step]
        print(lines)

        overlap = all()
        print(overlap)

    real_input = open("input.txt").readlines()
    overlaps = get_overlaps(real_input)
    priorities = [get_priority(i) for i in overlaps]

    assert sum(priorities) == 8202
