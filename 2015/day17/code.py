from itertools import combinations

def read_file(filename):
    with open(filename, 'r') as file:
        file_content = []
        for line in file:
            file_content.append(line.rstrip())
        
    return file_content

def parse_file(file):
    return [int(line) for line in file]

# easy ineffective way lol
def get_combinations(sizes, total):
    combos = []
    for i in range(len(sizes)):
        for c in combinations(sizes, i):
            if sum(c) == total:
                combos.append(c)
    
    return combos

def main():
    file = read_file('input.txt')
    sizes = parse_file(file)
    combos = get_combinations(sizes, total=150)
    min_length = min([len(c) for c in combos])
    min_length_combos = [c for c in combos if len(c) == min_length]
    print(f'Part 1: {len(combos)}')
    print(f'Part 2: {len(min_length_combos)}')

if __name__ == '__main__':
    main()