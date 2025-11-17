WIDTH = 100
HEIGHT = 100
NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
ALWAYS_ON = {(0, 0), (0, WIDTH-1), (HEIGHT-1, 0), (HEIGHT-1, WIDTH-1)}

def read_file(filename):
    with open(filename, 'r') as file:
        file_content = []
        for line in file:
            l = []
            for char in line.rstrip():
                l.append(char)
            file_content.append(l)
        
    return file_content

def parse_lights(file, part2):
    lights = [[cell == '#' for cell in line] for line in file]

    if part2:
        for i, j in ALWAYS_ON:
            lights[i][j] = True

    return lights

def count_on_neighbours(i, j, lights):
    on = 0

    for di, dj in NEIGHBORS:
        ni = i + di
        nj = j + dj
        if is_within_bounds(ni, nj):
            on += lights[ni][nj]
        
    return on

def is_within_bounds(i, j):
    return 0 <= i < HEIGHT and 0 <= j < WIDTH

def do_one_cycle(lights, part2):
    new_lights = [[False] * WIDTH for i in range(HEIGHT)]

    if part2:
        for i, j in ALWAYS_ON:
            new_lights[i][j] = True

    for i in range(HEIGHT):
        for j in range(WIDTH):
            if part2 and (i, j) in ALWAYS_ON:
                    continue

            on = count_on_neighbours(i, j, lights)
            
            if lights[i][j]:
                new_lights[i][j] = (on == 2 or on == 3)
            else:
                new_lights[i][j] = (on == 3)

    return new_lights

def cycle(lights, cycles, part2):
    for i in range(cycles):
        lights = do_one_cycle(lights, part2)
    
    return lights

def main():
    file = read_file('input.txt')

    # kinda ugly with all the part2 booleans
    lights1 = parse_lights(file, False)
    lights2 = parse_lights(file, True)

    final_lights1 = cycle(lights1, 100, False)
    final_lights2 = cycle(lights2, 100, True)

    print(f'Part 1: {sum(sum(row) for row in final_lights1)}')
    print(f'Part 2: {sum(sum(row) for row in final_lights2)}')

if __name__ == '__main__':
    main()