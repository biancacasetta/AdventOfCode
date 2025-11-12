
import re
import time

def read_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            file_content = line.rstrip()
        
    return file_content

def look_and_say(number, n):
    for i in range(n):
        # regex solution
        number = translate_regex(number)

        # for loop solution
        #number = translate_for_loop(number)

    return number

def translate_for_loop(number):
    result = ''
    current = number[0]
    counter = 0
    for j in range(len(number)):
        if number[j] == current:
                counter += 1
        else:
            result += str(counter) + current
            current = number[j]
            counter = 1
        
    result += str(counter) + current
    
    return result
    
def translate_regex(number):
    result = ''
    while number != '':
        start_char = number[0]
        leading = re.search('^' + start_char + '+', number)
        length = leading.end() - leading.start()

        result += str(length) + start_char
        number = number[length:]

    return result

def main():
    start = read_file('input.txt')

    s = time.time()

    print(f'Part 1: {len(look_and_say(start, 40))}')
    print(f'Part 2: {len(look_and_say(start, 50))}')

    e = time.time()
    print(e-s)

if __name__ == '__main__':
    main()