# take command line arguments
import sys
args = sys.argv
print(args)

# copying file
import shutil
# shutil.copyfile('a.txt','b.txt')

# # move/rename file
# import os   
# os.rename('b.txt','c.txt')

# All functions
# os.getcwd() - returns current working directory
# os.chdir(path) - changes current working directory to path
# os.listdir(path) - returns list of files in directory
# os.mkdir(path) - creates directory
# os.rmdir(path) - removes directory
# os.rename(old, new) - renames file or directory (can be used to move file)
# os.remove(path) - removes file
# os.system(cmd) - executes cmd in a subshell
# os.path.exists(path) - returns True if path exists
# os.path.isfile(path) - returns True if path is a file
# os.path.isdir(path) - returns True if path is a directory
# os.path.join(path1, path2) - joins two paths
# os.path.split(path) - splits path into (head, tail) tuple
# os.path.splitext(path) - splits path into (root, ext) tuple
# os.path.dirname(path) - returns directory name of path
# os.path.basename(path) - returns file name of path
# os.path.getsize(path) - returns size of file

# merge two file into new file
# with open('a.txt') as f1, open('b.txt') as f2, open('c.txt','w') as f3:
#     f3.writelines(f1.readlines())
#     f3.writelines(f2.readlines())



def wf():
    with open("./a.bin","wb") as f:
        for i in range(0,10):
            data = (" ".join([str(i*10+j) for j in range(1,11)]) + "\n").encode("ascii") 
            f.write(data)

def rf():
    with open("./a.bin","rb") as f:
        for x in f.readlines():
            print(sum(map(int,x.decode().split(" "))))
            
wf()
rf()