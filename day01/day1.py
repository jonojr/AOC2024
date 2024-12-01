
def number_count(number_list:list[int], search_number:int) -> int:
    return len(list(filter(lambda x: x==search_number, number_list)))


if __name__ == "__main__":
    left_locations = []
    right_locations = []

    with open("input.txt", "r") as input_file:
        location_pairs = input_file.read().split('\n')
        for location_pair in location_pairs:
            location1, location2 = location_pair.split('   ')
            left_locations.append(int(location1))
            right_locations.append(int(location2))

    sorted_left_locations = sorted(left_locations)
    sorted_right_locations = sorted(right_locations)

    part1 = 0
    for left, right in zip(sorted_left_locations, sorted_right_locations):
        if left > right:
            part1 += left - right
        else:
            part1 += right - left
    print(f"Part 1: {part1}")



    part2 = 0
    for left in sorted_left_locations:
        part2 += left * number_count(sorted_right_locations, left)
    print(f"Part 2: {part2}")
