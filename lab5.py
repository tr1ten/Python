def Q1():
    print(list("Hello"))
# Q1()
def Q2():
    a = "this is was sentence and was not a sentence"
    print([x for x in a.split(" ") if(a.count(" "+x+" ")>1) ][0])
# Q2()

def Q3():
    a,b = 'shubh','dhubh'
    print(",".join(set(a)&set(b)) if(set(a)&set(b)) else "No Common Characters")

# Q3()
def Q4():
    a = "this is the string we are considering"
    print("".join(sorted([x for x in set(a) if(a.count(x)==1 and x!=' ') ])),"".join(sorted([x for x in set(a) if(a.count(x)>1 and x!=' ') ])))


# Q4()

def Q5():
    st = "this is the string"
    sub = " the string"
    print(st.find(sub) if(st.find(sub)!=-1) else "Not Found")

Q5()