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

    list_left = []
    list_right = []

    for input in input_list:
        left, right = input.split('   ')
        list_left.append(int(left))
        list_right.append(int(right))
    
    list_left.sort()
    list_right.sort()

    return list_left, list_right


def calculate_list_distance(input_file):
    list_left, list_right = read_input(input_file)

    difference = sum(
        abs(left - right)
        for left, right in zip(list_left, list_right)
    )
    
    return difference

def calculate_similarity_score(input_file):
    list_left, list_right = read_input(input_file)
    
    occurences = collections.defaultdict(int)

    for right in list_right:
        occurences[right] += 1

    similarity_score = sum([
        item * occurences[item] for item in list_left
    ])

    return similarity_score


if __name__ == '__main__':
    args = parse_args()

    result = calculate_list_distance(args.input)
    print('List distance', result)

    result = calculate_similarity_score(args.input)
    print('Similarity score', result)
