def solution(s):
    count = 0 
    for char in s:
        if char == '(':
            count+=1
        else:
            if not count==0:
                count-=1
            else:
                return False
    return count==0
