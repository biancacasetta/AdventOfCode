 def read_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            file_content = [*line.rstrip()]

    return file_content

def move_floors(file_content):
    floor = 0
    basement = False
    for i, char in enumerate(file_content):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1

        if floor < 0 and not basement:
            basement = i + 1
    
    return floor, basement

def main():
    file_content = read_file('input.txt')
    floor, basement = move_floors(file_content)
    print(f'Part 1: {floor}')
    print(f'Part 2: {basement}')

if __name__ == '__main__':
    main()