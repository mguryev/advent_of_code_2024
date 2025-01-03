import argparse
import collections


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('input')

    return parser.parse_args()


def read_input(input_file):
    input_list = []

    with open(input_file, 'r') as file:
        input_list = file.readlines()

    reports = []

    for input in input_list:
        values = input.split(' ')

        reports.append([int(v) for v in values])
    
    return reports


def is_safe_report(report) -> bool:
    report_values = [
        (val, next_val) for val, next_val in zip(report, report[1:])
    ]


    return (
        all((b - a in {1, 2, 3} for a, b in report_values))
        or all ((a - b in {1, 2, 3} for a, b in report_values))
    )


def count_safe_reports(input_file):
    reports = read_input(input_file)
    filtered_reports = [report for report in reports if is_safe_report(report)]
    return len(filtered_reports)


def is_safe_report_with_dampener(report, allowed_diffs):
    exclusions = 0
    value = report[0]

    for next_value in report[1:]:
        if next_value - value in allowed_diffs:
            value = next_value
        else:
            exclusions += 1

            if exclusions > 1:
                return False
    
    return True


def count_safe_reports_with_dampener(input_file):
    reports = read_input(input_file)
    filtered_reports = [
        report for report in reports if 
            is_safe_report_with_dampener(report, allowed_diffs={1, 2, 3}) 
            or is_safe_report_with_dampener(list(reversed(report)), allowed_diffs={-1, -2, -3})
            or is_safe_report_with_dampener(report, allowed_diffs={-1, -2, -3})
            or is_safe_report_with_dampener(list(reversed(report)), allowed_diffs={1, 2, 3})
    ]

    return len(filtered_reports)


if __name__ == '__main__':
    args = parse_args()
    count = count_safe_reports(args.input)
    print(f'Safe reports: {count}')

    count = count_safe_reports_with_dampener(args.input)
    print(f'Safe reports with dampener: {count}')
