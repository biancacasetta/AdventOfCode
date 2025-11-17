WIDTH = 6
HEIGHT = 6

def read_file(filename):
    with open(filename, 'r') as file:
        file_content = []
        for line in file:
            l = []
            for char in line.rstrip():
                l.append(char)
            file_content.append(l)
        
    return file_content

def parse_lights(file):
    lights = {'on': [], 'off': []}
    for i, line in enumerate(file):
        l = []
        for j, char in enumerate(line):
            status = 'on' if char == '#' else 'off'
            lights[status] += [(i, j)]
    return lights

def get_neighbours(cell):
    neighbors = []
    for i in range(cell[0]-1, cell[0]+2):
        for j in range(cell[1]-1, cell[1]+2):
            c = (i, j)
            if is_out_of_bounds((i, j)):
                continue

            neighbors.append(c)
        
    return neighbors

def is_out_of_bounds(cell):
    return not (0 <= cell[0] < HEIGHT and 0 <= cell[1] < WIDTH)

def get_next_state(light):
    pass

def main():
    file = read_file('test_input.txt')
    lights = parse_lights(file)
    print(lights)

if __name__ == '__main__':
    main()