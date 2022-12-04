def sonar_sweep():
    handle = open("input.txt")

    higher_counter = 0
    previous = None

    for line in handle.readlines():
        value = int(line)

        if not previous:
            previous = value
            continue

        if value > previous:
            higher_counter += 1

        previous = value

    print(f"Number of times higher than previous: {higher_counter}")


if __name__ == '__main__':
    sonar_sweep()
