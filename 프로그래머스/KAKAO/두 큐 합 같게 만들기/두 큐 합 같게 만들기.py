def solution(queue1, queue2):
    count = 0
    a = sum(queue1)
    b = sum(queue2)
    
    total = a+b
    
    target = total // 2
    
    if (total % 2 != 0):
        return -1
    
    # 무한 루프 방지
    limit = (len(queue1) + len(queue2)) * 2
    
    while(a != target and count < limit):
        if(a>target):
            x = queue1.pop(0)
            queue2.append(x)
            
            a -= x
            b += x
            
        elif(a<target):
            x = queue2.pop(0)
            queue1.append(x)
            
            b -= x
            a += x
            
        count += 1
        
    if (a==target):
        return count
    
    return -1