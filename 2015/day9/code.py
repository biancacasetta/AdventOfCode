from itertools import permutations

def read_file(filename):
    with open(filename, 'r') as file:
        file_content = []
        for line in file:
            file_content.append(line.rstrip())
        
    return file_content

def format_content(file_content):
    distances = {}
    for l in file_content:
        pair, distance = l.split(' = ')
        city1, city2 = pair.split(' to ')
        distances.setdefault(city1, {})[city2] = int(distance)
        distances.setdefault(city2, {})[city1] = int(distance)

    return distances

def find_shortest_path(distances):
    shortest = float('inf')
    longest = float('-inf')
    cities = set(distances.keys())

    for route in permutations(cities):
        total_shortest, total_longest = 0, 0

        for i, city in enumerate(route):
            if i <= len(route) - 2:
                next = route[i+1]
                total_shortest += distances[city][next]
                total_longest += distances[city][next]
        
        if total_shortest < shortest:
            shortest = total_shortest
        if total_longest > longest:
            longest = total_longest

    return shortest, longest

def main():
    file_content = read_file('input.txt')
    distances = format_content(file_content)
    shortest, longest = find_shortest_path(distances)
    print(f'Part 1: {shortest}')
    print(f'Part 2: {longest}')
        

if __name__ == '__main__':
    main()