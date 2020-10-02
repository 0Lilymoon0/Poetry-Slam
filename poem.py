import random

def get_file_lines(filename):
    for i in range(len(filename)):
        read_poem = str(i + 1) + " " + filename[i]
    return read_poem

infile = open("poem.txt", "r")
get_file_lines(infile.read().splitlines())
infile.close
print("\n")

def lines_printed_backwards(lines_list):
    num_lines = len(lines_list)
    lines_list = lines_list[::-1]
    for i in range(len(lines_list)):
        backwards_poem = str(num_lines - i) + " " + lines_list[i]
        print(backwards_poem)
    return []

infile = open("poem.txt", "r")
lines_printed_backwards(infile.read().splitlines())
infile.close
print("\n")

def lines_printed_random(filename):
    num_lines = len(filename)
    for i in range(num_lines):
        random_select_line = random.randint(1, num_lines - 1)
        print(filename[random_select_line])
    return []

infile = open("poem.txt", "r")
poemList = infile.read().splitlines()
lines_printed_random(poemList)
infile.close
print("\n")