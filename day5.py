import argparse
import collections


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Input file path')
    return parser.parse_args()


def read_input(input_file):
    lines = []

    with open(input_file, 'r') as file:
        for line in file.readlines():
            lines.append(line.strip())

    rules = []
    manual_updates = []

    while len(lines) > 0:
        next_line = str(lines.pop(0))

        if next_line == "":
            break

        rules.append(next_line.split("|"))

    for line in lines:
        manual_updates.append(line.split(","))

    return rules, manual_updates


def calculate_manual_update(rules, manual_updates):
    rules_after = collections.defaultdict(set)

    for prior, after in rules:
        rules_after[prior].add(after)

    valid_updates = []
    for update in manual_updates:
        for idx, page in enumerate(update):
            update_before = set(update[:idx])
            update_after = set(update[idx+1:])

            if rules_after[page].intersection(update_before):
                break

        else:
            valid_updates.append(update)

    update_value = 0
    for update in valid_updates:
        mid_idx = len(update) // 2
        update_value += int(update[mid_idx])

    return update_value


def calculate_manual_update__fixed(rules, manual_updates):
    rules_after = collections.defaultdict(set)

    for prior, after in rules:
        rules_after[prior].add(after)
        
    valid_updates = []
    invalid_updates = []
    for update in manual_updates:
        for idx, page in enumerate(update):
            update_before = set(update[:idx])
            update_after = set(update[idx+1:])

            if rules_after[page].intersection(update_before):
                invalid_updates.append(update)
                break

        else:
            valid_updates.append(update)
    
    update_value = 0

    for update in invalid_updates:
        class Page:
            def __init__(self, number):
                self.number = number
            
            def __lt__(self, other):
                return (
                    other in rules_after[self.number]
                    or self.number not in rules_after[other.number]
                )
            
            def __repr__(self):
                return str(self.number)
            
        update = [Page(page) for page in update]
        update = sorted(update)
        update = [page.number for page in update]

        mid_idx = len(update) // 2
        update_value += int(update[mid_idx])

    return update_value


def run(args):
    rules, manual_updates = read_input(args.input)

    result = calculate_manual_update(rules, manual_updates)
    print(f"Manual update value: {result}")

    result = calculate_manual_update__fixed(rules, manual_updates)
    print(f"Manual update value (fixed): {result}")


if __name__ == '__main__':
    args = parse_args()
    run(args)
