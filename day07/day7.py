import itertools
import operator


def concat(a: int, b: int) -> int:
    return int(str(a) + str(b))

def check_valid(target: int, values:list[int], operators) -> bool:
    for possible_solution in itertools.product(operators, repeat=len(values) - 1):

        previous_val = values[0]
        for i in range(len(values) - 1):
            previous_val = possible_solution[i](previous_val, values[i + 1])

        if previous_val == target:
            return True

    return False


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        calibrations = [calibration.split(':') for calibration in input_file.read().split("\n")]

    part1 = 0
    for calibration in calibrations:
        target = int(calibration[0])
        values = list(map(int, calibration[1].strip().split(' ')))
        if check_valid(target, values, [operator.add, operator.mul]):
            part1 += target

    print(f"Part 1: {part1}")

    part2 = 0
    for calibration in calibrations:
        target = int(calibration[0])
        values = list(map(int, calibration[1].strip().split(' ')))
        if check_valid(target, values, [operator.add, operator.mul, concat]):
            part2 += target
    print(f"Part 2: {part2}")

