def count_calories():
    results = []
    for line in open("input.txt").readlines():
        line = line.strip()

        if line == "":
            results.append(0)
            continue

        if not len(results):
            results.append(int(line))
        else:
            results[-1] += int(line)

    return results


if __name__ == "__main__":
    results = count_calories()
    print(sum(sorted(results, reverse=True)[:3]))
