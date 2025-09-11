import re

def read_file(filename):
    with open(filename, 'r') as file:
        file_content = []
        for line in file:
            file_content.append(line)
        
    return file_content

def is_nice_1(line):
    return has_three_vowels(line) and has_double_letter(line) and has_no_forbidden_pairs(line)

def is_nice_2(line):
    return has_double_pairs(line) and has_sandwich(line)

def has_three_vowels(line):
    vowels = re.findall('[aeiou]', line)
    
    return len(vowels) >= 3

def has_double_letter(line):
    doubles = re.search('([a-z])\\1', line)

    return bool(doubles)

def has_no_forbidden_pairs(line):
    pairs = re.search('ab|cd|pq|xy', line)
    
    return not bool(pairs)

def has_double_pairs(line):
    double_pairs = re.search('([a-z]{2}).*?\\1', line)

    return bool(double_pairs)

def has_sandwich(line):
    sandwich = re.search('([a-z]).\\1', line)

    return bool(sandwich)

def main():#
    lines = read_file('input.txt')
    nice_lines_1 = [line for line in filter(is_nice_1, lines)]
    nice_lines_2 = [line for line in filter(is_nice_2, lines)]

    print(f'Part 1: {len(nice_lines_1)}')
    print(f'Part 2: {len(nice_lines_2)}')

if __name__ == '__main__':
    main()