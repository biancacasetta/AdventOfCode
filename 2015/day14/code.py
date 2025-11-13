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

def calculate_distance(reindeer, seconds):
    speed, time, rest = reindeer
    distance, s = 0, 0
    go = True

    while s < seconds:
        if go:
            if s + time - 1 < seconds:
                distance += speed * time
                s += time
                go = not go
            else:
                distance += speed
                s += 1
        else:
            if s + rest - 1 < seconds:
                s += rest
                go = not go
            else:
                s += 1
                  
    return distance

def race(reindeers, seconds):
    distances = {}
    for r, values in reindeers.items():
        d = calculate_distance(values, seconds)
        distances[r] = d
    
    return distances

def race2(reindeers, seconds):
    distances, points, counters = ({k: 0 for k in reindeers} for i in range(3))

    for s in range(seconds):
        for r, values in reindeers.items():
            speed, time, rest = values
            # once cycle is time + rest
            if counters[r] < time:
                distances[r] += speed
            elif counters[r] == time + rest - 1:
                counters[r] = 0
            
            counters[r] += 1
        
        #lead = max(distances, key=distances.get)
        #points[lead] += 1
    
    return distances, points

def main():
    file = read_file("test_input.txt")
    reindeers = parse_data(file)
    seconds = 1000 #2503
    results = race(reindeers, seconds)
    distances, points = race2(reindeers, seconds)
    #print(f'Part 1: {max(results.values())}')
    print(distances)
    print(f'Part 1: {max(distances.values())}')

if __name__ == '__main__':
    main()