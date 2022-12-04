def sonar_sweep():
    handle = open("input.txt")

    window_counter = 0
    previous_window = None

    data = handle.readlines()
    for i, line in enumerate(data):
        try:
            window_value = sum([int(s) for s in data[i:i+3]])
        except IndexError:
            break

        if not previous_window:
            previous_window = window_value
            continue

        if window_value > previous_window:
            window_counter += 1

        previous_window = window_value

    print(f"Number of times higher than previous: {window_counter}")


if __name__ == '__main__':
    sonar_sweep()
