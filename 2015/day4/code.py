import hashlib

def read_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            return line.rstrip()

def find_lowest_number(key, start, num):
    while True:
        new_key = key + str(num)
        res = hashlib.md5(new_key.encode())
        hashed = res.hexdigest()

        if hashed.startswith(start):
            return num
        
        num += 1

def main():
    key = read_file('input.txt')
    five = find_lowest_number(key, '00000', 1)
    print(f'Part 1: {five}')
    print(f'Part 2: {find_lowest_number(key, '000000', five)}')

if __name__ == '__main__':
    main()