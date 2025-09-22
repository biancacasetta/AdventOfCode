import re

def read_file(filename):
    with open(filename, 'r') as file:
        file_content = []
        for line in file:
            file_content.append(line.rstrip())
        
    return file_content

def parse_instructions(file_content):
    pattern = re.compile('^(turn on|turn off|toggle)')
    instructions = []
    for i in file_content:
        i1, j1, i2, j2 = [int(i) for i in re.findall('\\d+', i)]
        action = pattern.match(i).group(1)
        instructions.append([action, (i1, j1), (i2, j2)])
    
    return instructions

def change_light(instruction, lights):
    action, start, end = instruction
    actions = {'turn on': True, 'turn off': False}

    for row in range(start[0], end[0]+1):
        for col in range(start[1], end[1]+1):
            match action:
                case 'toggle':
                    lights[row][col] = not lights[row][col]
                case _:
                    lights[row][col] = actions[action]

def change_brightness(instruction, lights):
    action, start, end = instruction
    actions = {'turn on': 1, 'turn off': -1, 'toggle': 2}

    for row in range(start[0], end[0]+1):
        for col in range(start[1], end[1]+1):
            if lights[row][col] == 0 and action == 'turn off':
                continue
            
            lights[row][col] += actions[action]

def execute_all_instructions(instructions):
    lights = init_lights()
    for i in instructions:
        change_light(i, lights)

    brightness_lights = init_brightness()
    for i in instructions:
        change_brightness(i, brightness_lights)

    return lights, brightness_lights

def init_lights():
    return [[False for _ in range(1000)] for _ in range(1000)]

def init_brightness():
    return [[0 for _ in range(1000)] for _ in range(1000)]   

def main():
    instructions = parse_instructions(read_file('input.txt'))
    lights, brightness = execute_all_instructions(instructions)

    on_lights = sum([row.count(True) for row in lights])
    total_brightness = sum([sum(row) for row in brightness])

    print(f'Part 1: {on_lights}')
    print(f'Part 2: {total_brightness}')

if __name__ == '__main__':
    main()