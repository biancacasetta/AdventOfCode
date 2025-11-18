import re
import copy

def read_file(filename):
    with open(filename, 'r') as file:
        file_content = []
        for line in file:
            file_content.append(line.rstrip())
        
    return file_content

def parse_file(file):
    molecule = file[-1]
    replacements = {}

    for line in file:
        if not line:
            break

        k, v = line.split(' => ')
        replacements.setdefault(k, []).append(v)
    
    return replacements, molecule

def cycle_molecules(m, replacements):
    new_molecules = set()
    all_keys = re.compile('|'.join(replacements.keys()))

    for i in range(len(m)):
        res = all_keys.match(m, pos=i)

        if res:
            length = res.end() - i
            for r in replacements[res.group()]:
                new_m = m[:i] + r + m[i + length:]
                new_molecules.add(new_m)
    
    return new_molecules

def get_mol_from_electron(m, replacements):
    molecules = cycle_molecules('e', {'e': replacements['e']})
    steps = 1

    while m not in molecules:
        new = set()
        for i in molecules:
            new |= cycle_molecules(i, replacements)
        
        molecules = new
        round = steps * 1.50
        molecules -= {v for v in molecules if steps >= 2 and v[] != m[:steps]}
        print(len(molecules))
        print(steps)
        steps += 1
    
    return steps


def main():
    file = read_file('input.txt')
    replacements, molecule = parse_file(file)
    new_molecules = cycle_molecules(molecule, replacements)

    print(f'Part 1: {len(new_molecules)}')

    steps = get_mol_from_electron(molecule, replacements)
    print(f'Part 2: {steps}')


if __name__ == '__main__':
    main()