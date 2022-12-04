def main(positions):
    min_fuel_cost = None

    for target_position in range(max(crab_submarine_positions)):
        target_position_cost = 0
        for position in crab_submarine_positions:
            fuel_cost = sum([pos + 1 for pos in range(abs(position - target_position))])

            target_position_cost += fuel_cost

        if not min_fuel_cost or target_position_cost < min_fuel_cost:
            min_fuel_cost = target_position_cost

    return min_fuel_cost


def fuel_cost(distance):
    pass


if __name__ == '__main__':
    handle = open("input.txt")
    crab_submarine_positions = [int(i) for i in handle.read().split(",")]

    cheapest = find_cheapest_path(crab_submarine_positions)
    print(cheapest)
