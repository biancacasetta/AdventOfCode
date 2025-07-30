moves = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}

def read_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            file_content = [*line.rstrip()]
        
    return file_content

def separate_paths(file_content):
    santa_path = file_content[::2]
    robo_path = file_content[1::2]

    return santa_path, robo_path

def deliver_presents(path):
    i, j = 0, 0
    houses = set()
    houses.add((i, j))

    for move in path:
        m = moves[move]
        i += m[0]
        j += m[1]
            
        houses.add((i, j))
    
    return houses

def main():
    file_content = read_file('input.txt')
    print(f'Part 1: {len(deliver_presents(file_content))}')

    santa, robo = separate_paths(file_content)
    houses = deliver_presents(santa)
    houses |= deliver_presents(robo)

    print(f'Part 2: {len(houses)}')

if __name__ == '__main__':
    main()