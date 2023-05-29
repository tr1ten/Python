import string


def count(s):
    up = 0
    low=0
    for x in s:
        if(x.isupper()):
            up+=1
        else:
            low+=1
    print(f"The number of upper case letters are {up} and the number of Lower case letters are {low}")

# count("HeLlo")

def palindrome(s):
    rev = s[::-1]

    return s == rev
    
# print(palindrome("nitin"))

def ispangram(str1):
    alphabet=string.ascii_lowercase
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())
 
# print ( ispangram('The quick brown fox jumps over the lazy dog')) 

def abc():
    x = 76
    y = 2.6
    str1= "hi!"

print(abc.__code__.co_nlocals)