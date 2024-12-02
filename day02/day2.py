import itertools
from typing import Iterable


def safe_change(val1:int, val2: int) -> bool:
    return 1 <= abs(val1-val2) <= 3


def safe_report(report: Iterable[int]) -> bool:
    all_steps_safe = all([safe_change(val1, val2) for val1, val2 in itertools.pairwise(report)])
    all_increasing = all([val1 < val2 for val1, val2 in itertools.pairwise(report)])
    all_decreasing = all([val1 > val2 for val1, val2 in itertools.pairwise(report)])
    return all_steps_safe and (all_increasing or all_decreasing)


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        reports = input_file.read().split('\n')
        reports = [
            list(map(lambda x: int(x), levels.split())) for levels in reports
        ]


    report_safe = [
        safe_report(report)
        for report in reports
    ]

    print(f"Part 1: {sum(report_safe)}")


    report_safe_with_damper = []
    for report in reports:
        safe = safe_report(report)

        if not safe:
            for report_permutation in itertools.combinations(report, len(report) - 1):
                safe = safe_report(report_permutation)
                if safe:
                    break

        report_safe_with_damper.append(safe)

    print(f"Part 2: {sum(report_safe_with_damper)}")

