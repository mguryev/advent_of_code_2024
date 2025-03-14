import argparse
import re


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Input file path')
    return parser.parse_args()


def read_input(input_file):
    with open(input_file, 'r') as file:
        return file.readlines()


def parse_operations(line: str, operations_patterns: dict[str, re.Pattern]) -> list[tuple[str, int, list[str]]]:
    operations = []
    for op_type, pattern in operations_patterns.items():
        for match in pattern.finditer(line):
            operations.append((op_type, match.start(), match.groups()))

    return sorted(operations, key=lambda x: x[1])


def process_multiplications(lines):
    total_sum = 0
    mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r'don\'t\(\)')
    
    # Default state: multiplications are enabled
    multiply_enabled = True
    
    for line in lines:
        # Find all control instructions and multiplication statements
        # along with their positions in the line
        operations = parse_operations(line, {
            'do': do_pattern,
            'dont': dont_pattern,
            'mul': mul_pattern,
        })
        
        # Process operations in order
        for op_type, _, op_data in operations:
            if op_type == 'do':
                multiply_enabled = True
            elif op_type == 'dont':
                multiply_enabled = False
            elif op_type == 'mul' and multiply_enabled:
                factor1, factor2 = op_data
                product = int(factor1) * int(factor2)
                total_sum += product
    
    return total_sum


def main():
    args = parse_args()
    lines = read_input(args.input)
    result_sum = process_multiplications(lines)
    
    print(f"Sum of all multiplication results: {result_sum}")


if __name__ == '__main__':
    main()
