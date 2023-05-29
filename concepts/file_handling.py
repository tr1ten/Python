# read text from file
import os
def main():
    print("hey")
    print(os.path.getsize("a.txt"))
    r1 = open('a.txt')
    w1 = open('b.txt','a')
    w1.writelines(r1.readlines())
    r1.close()
    w1.close()

if __name__=="__main__":
    main()