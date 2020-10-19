def isperfect(number):
    s=0
    for i in range(1,number):
        if(number%i==0):
            s=s+i

    if(s==number):
        return True
    else:
        return False

def printperfect(start,end):
    for j in range(start,end+1):
        if(isperfect(j)):
            print("Ans: ",j)


start=int(input())
end=int(input())
printperfect(start,end)
