import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Input file path')
    return parser.parse_args()


def read_input(input_file):
    lines = []

    with open(input_file, 'r') as file:
        for line in file.readlines():
            lines.append([c for c in line.strip()])

    return lines


def search_for_xmas(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    window_size = 4

    verticals = [
        [[row, col] for row in range(window_size)] for col in range(window_size)
    ]
    horizontals = [
        [[row, col] for col in range(window_size)] for row in range(window_size)
    ]

    diags = [
        list([i, i] for i in range(window_size)),
        list([i, window_size - i - 1] for i in range(window_size)),
    ]

    match_patterns = horizontals + verticals + diags

    def windows():
        for row in range(0, num_rows - window_size + 1):
            for col in range(num_cols - window_size + 1):
                yield row, col

    matches = set()
    match_count = 0

    for start_row, start_col in windows():
        for pattern in match_patterns:
            value = ""
            key = ""

            for row, col in pattern:
                value += matrix[start_row + row][start_col + col]
                key += f"[{start_row + row},{start_col + col}]"

            if value == "XMAS":
                matches.add(f"{key}")
                match_count += 1
            if value == "SAMX":
                matches.add(f"{key}")
                match_count += 1

    return len(matches)


def search_for_cross_mas(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    window_size = 3

    pattern = [[0,0], [0,2], [1,1], [2,0], [2,2]]
    expected_values = {
        "MMASS",
        "MSAMS",
        "SSAMM",
        "SMASM",
    }

    def windows():
        for row in range(0, num_rows - window_size + 1):
            for col in range(num_cols - window_size + 1):
                yield row, col

    matches = set()

    for start_row, start_col in windows():
        value = ""
        key = ""

        for row, col in pattern:
            value += matrix[start_row + row][start_col + col]
            key += f"[{start_row + row},{start_col + col}]"

        if value in expected_values:
            matches.add(f"{key}")

    return len(matches)


def run(args):
    matrix = read_input(args.input)

    result = search_for_xmas(matrix)
    print(f"XMAS found: {result}")

    result   = search_for_cross_mas(matrix)
    print(f"Cross Mas found: {result}")



if __name__ == '__main__':
    args = parse_args()
    run(args)
