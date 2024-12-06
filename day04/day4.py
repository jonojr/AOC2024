def check_part_1(wordsearch:list[str], row: int, column:int, checkword = "XMAS") -> int:
    check_len = len(checkword)
    row_len = len(wordsearch)
    column_len = len(wordsearch[0])
    try:
        row_val = wordsearch[row][column:column + check_len]
    except IndexError:
        row_val = ""

    try:
        column_val = "".join([row[column] for row in wordsearch[row:row + check_len]])
    except IndexError:
        column_val = ""

    try:
        diagonal_val = ""
        for x in range(check_len):
            diagonal_val +=  wordsearch[row + x][column + x]
            if row + x >= row_len or column + x >= column_len:
                raise IndexError
    except IndexError:
        diagonal_val = ""

    try:
        diagonal_val_2 = ""
        for x in range(check_len):
            diagonal_val_2 +=  wordsearch[row + x][column - x]

            if row + x >= row_len or column - x < 0:
                raise IndexError
    except IndexError:
        diagonal_val_2 = ""

    reverse_checkword = checkword[::-1]
    count_of_matches = sum([
        row_val == checkword,
        column_val == checkword,
        diagonal_val == checkword,
        diagonal_val_2 == checkword,
        row_val == reverse_checkword,
        column_val == reverse_checkword,
        diagonal_val == reverse_checkword,
        diagonal_val_2 == reverse_checkword,
    ])
    return count_of_matches


def check_part_2(wordsearch:list[str], row: int, column:int) -> int:
    row_len = len(wordsearch)
    column_len = len(wordsearch[0])
    try:
        diagonal_val = ""
        for x in range(3):
            diagonal_val +=  wordsearch[row + x][column + x]
            if row + x >= row_len or column + x >= column_len:
                raise IndexError
    except IndexError:
        diagonal_val = ""

    try:
        diagonal_val_2 = ""
        for x in range(3):
            diagonal_val_2 +=  wordsearch[row + x][column + 2 - x]

            if row + x>= row_len or column + 2 - x < 0:
                raise IndexError
    except IndexError:
        diagonal_val = ""

    return diagonal_val in ("MAS", "SAM") and diagonal_val_2 in ("SAM", "MAS")


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        word_search = input_file.read().split()

    rows = len(word_search)
    columns = len(word_search[0])

    part1 = 0
    part2 = 0

    for row in range(rows):
        for column in range(columns):
            part1 += check_part_1(word_search, row, column)
            part2 += check_part_2(word_search, row, column)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
