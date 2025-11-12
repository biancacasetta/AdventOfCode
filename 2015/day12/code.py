import re
import json

def read_file(filename):
    with open(filename, 'r') as file:
        file_content = ''
        for line in file:
            file_content += line
        
    return file_content

def extract_numbers(file_content, remove_red):
    if remove_red:
        content = json.loads(file_content)
        cleaned = remove_red_values(content)
        file_content = json.dumps(cleaned)

    numbers = re.findall(r'-*\d+', file_content)
    numbers = [int(i) for i in numbers]

    return numbers

def remove_red_values(content):
    if isinstance(content, dict):
        if "red" in content.values():
            return None
        
        new = {k: remove_red_values(v) for k, v in content.items()}
        return new
    elif isinstance(content, list):
        return [remove_red_values(i) for i in content]
    else:
        return content

def main():
    content = read_file("input.txt")
    all_numbers = extract_numbers(content, False)
    all_nonred_numbers = extract_numbers(content, True)

    print(f'Part 1: {sum(all_numbers)}')
    print(f'Part 2: {sum(all_nonred_numbers)}')

if __name__ == '__main__':
    main()