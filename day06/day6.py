from enum import IntEnum


class Direction(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

def location_out_of_bounds(location: tuple[int, int], max_rows, max_cols):
    row, column = location
    if row < 0 or row > max_rows:
        return True
    if column < 0 or column > max_cols:
        return True
    return False

def get_next_location(location: tuple[int, int], direction: Direction) -> tuple[int, int]:
    if direction == Direction.NORTH:
        return location[0] - 1, location[1]
    if direction == Direction.EAST:
        return location[0], location[1] + 1
    if direction == Direction.SOUTH:
        return location[0] + 1, location[1]
    if direction == Direction.WEST:
        return location[0], location[1] - 1


def check_grid_loops(grid:list[str]) -> bool:
    location: tuple[int, int] = (-1, -1)
    facing = Direction.NORTH

    # Find starting location
    for row_num in range(len(grid)):
        row = grid[row_num]
        if '^' in row:
            column_num = row.find('^')

            location = (row_num, column_num)
            break

    guard_visited_locations = {(*location, facing)}

    next_location = get_next_location(location, facing)
    next_item = grid[next_location[0]][next_location[1]]

    try:
        while not location_out_of_bounds(next_location, len(grid), len(grid[0])):
            while next_item != '#' and not location_out_of_bounds(location, len(grid), len(grid[0])):
                location = next_location

                if (*location, facing) in guard_visited_locations:
                    return True
                guard_visited_locations.add((*location, facing))
                next_location = get_next_location(location, facing)

                if location_out_of_bounds(next_location, len(grid), len(grid[0])):
                    raise Exception
                next_item = grid[next_location[0]][next_location[1]]

            facing = (facing + 1) % 4
            next_location = get_next_location(location, facing)
            next_item = grid[next_location[0]][next_location[1]]
    except Exception:
        pass
    return False


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        grid = input_file.read().split("\n")

    location:tuple[int, int] = (-1, -1)
    facing = Direction.NORTH

    # Find starting location
    for row_num in range(len(grid)):
        row = grid[row_num]
        if '^' in row:
            column_num = row.find('^')

            location = (row_num, column_num)
            break

    guard_visited_locations = {location}

    next_location = get_next_location(location, facing)
    next_item = grid[next_location[0]][next_location[1]]

    try:
        while not location_out_of_bounds(next_location, len(grid), len(grid[0])):
            while next_item != '#' and not location_out_of_bounds(location, len(grid), len(grid[0])):
                location = next_location
                guard_visited_locations.add(location)
                next_location = get_next_location(location, facing)

                if location_out_of_bounds(next_location, len(grid), len(grid[0])):
                    raise Exception
                next_item = grid[next_location[0]][next_location[1]]


            facing = (facing + 1) % 4
            next_location = get_next_location(location, facing)
            next_item = grid[next_location[0]][next_location[1]]
    except Exception:
        pass

    part1 = len(guard_visited_locations)

    print(f"Part 1: {part1}")

    part2 = 0
    for location in guard_visited_locations:
        old_row = grid[location[0]]
        grid[location[0]] = f'{old_row[:location[1]]}#{old_row[location[1]:]}'
        # print(old_row, location, grid[location[0]])
        part2 += check_grid_loops(grid)
        grid[location[0]] = old_row
    print(f"Part 2: {part2}")

