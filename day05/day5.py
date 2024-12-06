from collections import defaultdict


def build_rules_lookup(ordering_rules:str) -> defaultdict[int, list]:
    rules_lookup = defaultdict(list)

    for rule in ordering_rules.split():
        key, value = rule.split('|')
        rules_lookup[int(key)].append(int(value))

    return rules_lookup


def update_valid(rules: defaultdict[int, list], update:list[int]) -> bool:
    for i in range(len(update)):
        current_page = update[i]
        previous_pages = update[:i]

        for required_page in rules[current_page]:

            if required_page in previous_pages:
                return False
    return True


def fix_invalid_update(rules: defaultdict[int, list], update:list[int]) -> list[int]:
    fixed_update = []
    values_in_update = set(update)

    while values_in_update:
        values_in_update_list = list(values_in_update)
        for value in values_in_update_list:
            if len(list(filter(lambda x: x in values_in_update, rules[value]))) > 0:
                continue
            fixed_update.append(value)
            values_in_update.remove(value)

    return fixed_update


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        ordering_rules, updates = input_file.read().split("\n\n")

    part1 = 0
    part2 = 0

    rules_lookup = build_rules_lookup(ordering_rules)

    for update in updates.split():
        update = list(map(int, update.split(',')))
        valid = update_valid(rules_lookup, update)

        if valid:
            part1 += int(update[len(update)//2])
        else:
            part2 += fix_invalid_update(rules_lookup, update)[len(update)//2]

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
