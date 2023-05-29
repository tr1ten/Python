def read_file():
    file = "example.txt"
    with open(file,"r") as f:
        print(f.read())
# read_file()

def read_file_line():
    file = "example.txt"
    res = []
    with open(file,"r") as f:
        while(True):
            line = f.readline()
            if(not line): break;
            res.append(line)
    print(res)
read_file_line()
from itertools import zip_longest
def merge_file():
    f1 = open('f1.txt','r');
    f2 = open('f2.txt','r')
    o2 = open('output.txt','w')
    for l1,l2 in zip_longest(f1.readlines(),f2.readlines(),fillvalue=""):
        o2.write(l1+l2)
    o2.close()
    f1.close()
    f2.close()

# merge_file()
def count_words():
    file = input()
    try:
        f = open(file)
    except: pass
    s = f.read()
    f.close()
    res = 0
    for x in s.split(" "):
        res += len(x.split(","))
    print(res)
# count_words()
def gen_files():
    for x in range(0,26):
        open(chr(x+ord('a'))+".txt",'w').close()
gen_files()
import string

def create_alphabet_file(num_per_line, filename):
    """Creates a file containing the English alphabet with specified number of letters per line."""
    with open(filename, 'w') as file:
        alphabet = string.ascii_uppercase
        for i in range(0, len(alphabet), num_per_line):
            file.write(alphabet[i:i+num_per_line] + '\n')
