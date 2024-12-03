import re

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        program = input_file.read()

    matches = re.finditer('mul\((\d+),(\d+)\)', program)


    result = 0
    for match in matches:
        val1, val2 = match.groups()
        result += int(val1) * int(val2)

    print(f"Part 1: {result}")


    removed_disabled, _ = re.subn("don\'t\(\).*?do\(\)", "", program, flags=re.DOTALL)

    matches = re.finditer('mul\((\d+),(\d+)\)', removed_disabled)
    result2 = 0
    for match in matches:
        val1, val2 = match.groups()
        result2 += int(val1) * int(val2)
    print(f"Part 2: {result2}")
