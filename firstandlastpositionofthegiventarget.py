def position(s,t):
    for i in range(len(s)):
        if s[i]==t:
            start=i
            while i+1<len(s) and s[i+1]==t:
                i+=1
            return[start,i]
    return[12]
position([1,2,3,4,5,6,7,8,8,8,8,8,8,8,0,10,10,8,12],8)
