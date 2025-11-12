from itertools import permutations

def read_file(filename):
    with open(filename, 'r') as file:
        file_content = []
        for line in file:
            file_content.append(line.rstrip())
        
    return file_content

def parse_data(file_content, myself):
    graph = {}
    for line in file_content:
        word_list = line.rstrip('.').split()
        name1 = word_list[0]
        name2 = word_list[-1]
        happiness = int(word_list[3])

        if "lose" in word_list:
            happiness *= -1
            
        graph.setdefault(name1, {})[name2] = happiness
    
    if myself:
        keys = list(graph.keys())
        for k in keys:
            graph.setdefault('Me', {})[k] = 0
            graph[k]['Me'] = 0
    
    return graph

def get_cycle_permutations(values):
    pivot = values.pop()
    perms = [list(p) + [pivot] for p in permutations(values)]

    return perms

def get_happiness(order, graph):
    happiness = 0
    for i, name in enumerate(order):
        next = order[i + 1] if name != order[-1] else order[0]
        happiness += graph[name][next]
        happiness += graph[next][name]

    return happiness

def get_max_happiness(graph):
    h = []
    for p in get_cycle_permutations(list(graph.keys())):
        h.append(get_happiness(p, graph))
    
    return max(h)

def main():
    file = read_file("input.txt")
    graph = parse_data(file, False)
    graph_with_me = parse_data(file, True)

    print(f'Part 1: {get_max_happiness(graph)}')
    print(f'Part 2: {get_max_happiness(graph_with_me)}')

if __name__ == '__main__':
    main()