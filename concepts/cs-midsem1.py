ADMIN_USER = 'admin'
ADMIN_PASSWORD = 'admin'

DB = {
    ADMIN_USER:ADMIN_PASSWORD
}
def register():
    F = 0
    user = input("mail: ")
    passowrd = input("password: ")
    if(user not in DB):
        ask = input("user doesn't esist, want to create new one (Y/N)?: ")
        if(ask.lower()=='y'): DB[user] = passowrd;
    if(user in DB and DB[user]==passowrd):
        F = 1 + (user==ADMIN_USER)
    return F

TOPICS = {
    "maths": [{
        "q": "1+1?",
        "a": "2",
        "score": 1,
    }],
    "science": [{
        "q": "earth is flat?(Y/N)",
        "a": "n",
        "score": 2,
    }],
    
}
def main():
    print("\n\t Welcome to Quiz\t\n")
    print("Authenticate yourself")
    f = register()
    if(not f):
        print("Failed, try again")
        return;
    print('Successfuly registered as ' + ('user' if f==1 else "admin"))
    print("Available topic")
    for i in range(len(TOPICS)): print(f'{i+1}. {list(TOPICS.keys())[i]}')
    t = int(input("Select (1-{}):".format(len(TOPICS))))
    if(t<=0 or t>len(TOPICS)):
        print("Invalid, Try again")
        return ;
    t  = list(TOPICS.keys())[t-1]
    score = 0
    for i,q in enumerate(TOPICS[t]):
        print(f"Q{i+1}. {q['q']} ")
        if(f==1):
            ans = input( "Your ans : ")
            score += (ans.lower()==q['a'])
        else:
            ans = input("modify(m)/delete(d) : ")
            if(ans not in ["m","d"]): print("Invalid"); return;
            if(ans=='m'):
                nq = input("new quesiton : ")
                ns  = input("new ans : ")
                q['q']= nq
                q['a'] = ns
            else:
                TOPICS[t].remove(q)
    if(f==1): print("Final Score ",score)
    else: print("All operation done")
    if(input("again? (y/n): ").lower() == 'y'): main()
    
    
main();