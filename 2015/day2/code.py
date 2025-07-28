def read_file(filename):
    with open(filename, 'r') as file:
        file_content = []
        for line in file:
            file_content.append(line.rstrip())
        
    return file_content

def parse_content(file_content):
    measurements = []
    for line in file_content:
        measurements.append([int(n) for n in line.split('x')])
    
    return measurements

def calculate_wrapping_paper(measurements):
    total_paper = 0
    for l, w, h in measurements:
        total_paper += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    
    return total_paper

def calculate_ribbon(measurements):
    total_ribbon = 0
    for l, w, h in measurements:
        total_ribbon += l*w*h
        m = [l, w, h]
        m.remove(max(l, w, h))
        total_ribbon += sum(2*n for n in m)
    
    return total_ribbon       

def main():
    measurements = parse_content(read_file('input.txt'))

    print(f'Part 1: {calculate_wrapping_paper(measurements)}')
    print(f'Part 2: {calculate_ribbon(measurements)}')

if __name__ == '__main__':
    main()