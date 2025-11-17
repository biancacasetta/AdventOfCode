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
    lights = []
    for line in file:
        l = []
        for char in line:
            status = 1 if char == '#' else 0
            l.append(status)
        lights.append(l)
    
    return lights

def main():
    file = read_file('test_input.txt')
    lights = parse_lights(file)
    print(lights)

if __name__ == '__main__':
    main()