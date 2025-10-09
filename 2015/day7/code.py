import re

def read_file(filename):
    with open(filename, 'r') as file:
        file_content = []
        for line in file:
            file_content.append(line.rstrip())
        
    return file_content

def parse_instructions(file_content):
    patterns = {
        'assign': '^(\\d+|[a-z]+) -> (.+)',
        'not': '^NOT (.+) -> (.+)',
        'andor': '(.+) (AND|OR) (.+) -> (.+)',
        'shift': '(.+) (LSHIFT|RSHIFT) (\\d+) -> (.+)'
        }

    instructions = []

    for i in file_content:
        for k, v in patterns.items():
            m = re.search(v, i)

            if m is not None:
                groups = [int(i) if i.isnumeric() else i for i in list(m.groups())]       
                match k:
                    case 'assign' | 'not':
                        instructions.append([k.upper(), groups[0], groups[1]])
                    case 'andor' | 'shift':
                        instructions.append([groups[1], (groups[0], groups[2]), groups[3]])

                break

    wires = {i[-1]: None for i in instructions}
    
    return instructions, wires

def check_source_type(source, wires):
    match source:
        case str():
            return wires[source] is not None
        case tuple():
            return check_source_type(source[0], wires) and check_source_type(source[1], wires)
        case int():
            return True

def run_instruction(instruction, wires):
    action, source, destination = instruction

    if check_source_type(source, wires) and wires[destination] is None:
        match action:
            case 'ASSIGN':
                result = source if type(source) is int else wires[source]
                wires[destination] = result
            case 'NOT':
                wires[destination] = (~wires[source]) & 0xFFFF
            case 'AND':
                a = wires[source[0]] if type(source[0]) is str else source[0]
                wires[destination] = a & wires[source[1]]
            case 'OR':
                wires[destination] = wires[source[0]] | wires[source[1]]
            case 'LSHIFT':
                wires[destination] = wires[source[0]] << source[1]
            case 'RSHIFT':
                wires[destination] = wires[source[0]] >> source[1]

def run_all_instructions(instructions, wires):
    while None in wires.values():
        for i in instructions:
            run_instruction(i, wires)

def reset_wires(wires):
    for wire, signal in wires.items():
        wires[wire] = None

def main():
    file_content = read_file('input.txt')
    instructions, wires = parse_instructions(file_content)
    run_all_instructions(instructions, wires)

    a = wires['a']
    print(f'Part 1: {a}')

    reset_wires(wires)
    wires['b'] = a
    run_all_instructions(instructions, wires)
    print(f'Part 2: {wires['a']}')

if __name__ == '__main__':
    main()