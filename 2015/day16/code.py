evidence = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

def read_file(filename):
    with open(filename, 'r') as file:
        file_content = []
        for line in file:
            file_content.append(line.rstrip())
        
    return file_content

def parse_aunts(file):
    aunts = {}
    for line in file:
        aunt, data = line.split(': ', maxsplit=1)
        aunt = int(aunt.split()[1])
        props = data.split(', ')
        props = {k: int(v) for k, v in [prop.split(': ') for prop in props]}
        aunts[aunt] = props
    
    return aunts

def is_right_aunt(num, props, part2):
    for k, v in props.items():
        if part2:
            match k:
                case 'cats' | 'trees':
                    if props[k] <= evidence[k]:
                        break
                case 'pomeranians' | 'goldfish':
                    if props[k] >= evidence[k]:
                        break
                case _:
                    if props[k] != evidence[k]:
                        break
        else:
            if props[k] != evidence[k]:
                break
    else:
        return num

    return None

def find_aunt(aunts, part2=False):
    for a in aunts:
        if is_right_aunt(a, aunts[a], part2):
            return a

    return None         

def main():
    file = read_file('input.txt')
    aunts = parse_aunts(file)
    print(f'Part 1: {find_aunt(aunts)}')
    print(f'Part 2: {find_aunt(aunts, True)}')

if __name__ == '__main__':
    main()