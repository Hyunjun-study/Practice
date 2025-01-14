def solution(a, b, c, d):
    my_list = [a,b,c,d]
    my_list.sort()
    
    n1 = my_list[0]
    n2 = my_list[1]
    n3 = my_list[2]
    n4 = my_list[3]
    
    if n1 == n2 == n3 == n4:
        return n1*1111
    elif n1 == n2 and n3 == n4:
        return (n1+n3)*abs(n1-n3)
    
    elif (n1 == n2 and n3 != n4 and n2 != n3):
        return n3*n4
    elif (n1 != n4 and n2 == n3 and n1!=n2 and n3!=n4):
        return n1*n4
    elif (n1 != n2 and n3 == n4 and n2!=n3):
        return n1*n2
    elif (n1==n2==n3 and n1!=n4):
        return (10*n1+n4)**2
    elif (n2==n3==n4 and n2 != n1):
        return (10*n2+n1)**2   
    else:
        return n1
    
    
