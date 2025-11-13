def read_file(filename):
    with open(filename, 'r') as file:
        file_content = []
        for line in file:
            file_content.append(line.rstrip('.\n'))
        
    return file_content

def parse_data(file):
    reindeers = {}

    for line in file:
        words = line.split()
        name = words[0]
        numbers = [int(i) for i in words if i.isnumeric()]
        reindeers[name] = numbers
    
    return reindeers

def race(reindeers, seconds):
    distances, points, counters = ({k: 0 for k in reindeers} for i in range(3))

    for s in range(seconds):
        move_reindeers(reindeers, counters, distances)
        add_points(distances, points)
    
    return distances, points

def move_reindeers(reindeers, counters, distances):
    for r, values in reindeers.items():
        speed, time, rest = values
        if counters[r] < time:
            distances[r] += speed
        elif counters[r] == time + rest - 1:
            counters[r] = 0
            continue
        
        counters[r] += 1

def add_points(distances, points):
    lead = max(distances.values())
    for name, d in distances.items():
        if d == lead:
            points[name] += 1

def main():
    file = read_file("input.txt")
    reindeers = parse_data(file)
    seconds = 2503
    distances, points = race(reindeers, seconds)
    print(f'Part 1: {max(distances.values())}')
    print(f'Part 2: {max(points.values())}')

if __name__ == '__main__':
    main()