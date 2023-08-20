def sequence_generator(number):
    return [i ** 2 - i - 1 for i in range(2, number + 1)]


def closest_multiple(number, target):
    multiple = round(target / number)
    return [multiple, target - multiple * number]


def char_sign(number):
    return ('+', '-')[number < 0]


def uni_expansion(arr, i):
    prev_closest = 0
    for j in range(0, len(arr)):
        closest, difference = closest_multiple(i, arr[j])
        print(f"{i} * {closest} {char_sign(difference)} {abs(difference)}\t\t|\t Diff: {closest - prev_closest}", end="\n")
        print(f"    {i}\t*\t{closest}\t{char_sign(difference)}\t{abs(difference)}\t=\t{arr[j]}", end="\n")
        prev_closest = closest


def loop_expansions(arr, n, loop=False):
    if loop:
        for i in range(2, n + 1):
            uni_expansion(arr, i)
    else:
        uni_expansion(arr, n)


def __main__():
    sequence = sequence_generator(20)

    print(sequence, end="\n")
    loop_expansions(sequence, 15)
    print()


__main__()
