# Dice sum probability calculator
# Författare: Tobias Stridsberg
# Datum: 2024-08-22
def mode(x):
    x=sorted(x)
    g=[]
    d=[]
    counter=0
    common=[]
    for n in range(0,len(x)):
        if x[n] not in g:
            g.append(x[n])
            d.append(1)
        else:
            for v in range(0,len(g)):
                if x[n] == g[v]:
                    d[v]=d[v]+1
    for n in range(len(d)-1,-1,-1):
        if d[n] > counter:
            common=[]
            counter=d[n]
            common.append(g[n])
        if d[n] == counter:
            if g[n] not in common:
                common.append(g[n])
        d.pop()
        g.pop()
    x=''
    s=1
    antal=len(common)
    h=[]
    for i in range(1,len(common)+1):
        h.append(common[-i])
    common=h
    for common in common:
        x=x+str(common)
        if s != antal:
            x=x+"\n" 
        s+=1
    return x
def main():
    thelist=[]
    user_input = input().split(" ")
    DiceSides1 = int(user_input[0])
    DiceSides2 = int(user_input[1])
    for i in range(1,DiceSides1+1):
        for ii in range(1,DiceSides2+1):
            thelist.append(i+ii)
    print(mode(thelist))
if __name__ == "__main__":
    main()