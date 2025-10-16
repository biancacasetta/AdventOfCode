import re

def read_file(filename):
    with open(filename, 'r') as file:
        file_content = []
        for line in file:
            file_content.append(line.rstrip())
        
    return file_content

def clean_strings(strings):
    cleaned_strings = []
    patterns = r'(\\x[a-f0-9]{2}|\\"|\\\\)'

    for s in strings:
        s = s.lstrip('"').rstrip('"')
        new_string = re.sub(patterns, '.', s)
        cleaned_strings.append(new_string)
    
    return cleaned_strings

def expand_strings(strings):
    expanded_strings = []
    patterns = r'(\"|\\)' 

    for s in strings:
        new_string = re.sub(patterns, '..', s)
        expanded_strings.append('"' + new_string + '"')
    
    return expanded_strings

def calculate_difference(strings, parsed_strings, action):
    og_lengths = [len(s) for s in strings]
    new_lengths = [len(s) for s in parsed_strings]

    if action == 'clean':
        diff = sum(og_lengths) - sum(new_lengths)
    else:
        diff = sum(new_lengths) - sum(og_lengths)

    return diff

def main():
    strings = read_file('input.txt')
    cleaned = clean_strings(strings)
    expanded = expand_strings(strings)

    print(f'Part 1: {calculate_difference(strings, cleaned, 'clean')}')
    print(f'Part 2: {calculate_difference(strings, expanded, 'expand')}')

if __name__ == '__main__':
    main()