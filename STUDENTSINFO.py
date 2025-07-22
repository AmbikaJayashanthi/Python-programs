
def addstu():
    i=4
    names=[]
    marks=[]
    per=[]
    while i>0:
        m=[]
        name=input("Enter name:")
        names.append(name)
        mark1=int(input("OS marks:"))
        m.append(mark1)
        mark2=int(input("CA marks:"))
        m.append(mark2)
        mark3=int(input("DS marks:"))
        m.append(mark3)
        marks.append(m)
        p=sum(m)/3
        per.append(p)
        st=list(zip(names,marks,per))
        i=i-1
    print(st)
addstu()

