def solution(priorities, location):
    answer = 0
    lenl=len(priorities)
    processes = list(range(lenl))
    queue=list(zip(processes,priorities))
    priority_queue = []
    while queue:
        count=0
        for quevalue in queue[1:]:
            if queue[0][1]<quevalue[1]:
                count+=1
                break
            else:
                continue
        tempvalue=queue.pop(0)
        if count>0:
                queue.append(tempvalue)
        else:
            priority_queue.append(tempvalue)

    loc_count = 1
    for pq_value in priority_queue:
        if pq_value[0] == location:
            answer = loc_count
            loc_count+=1
    return answer
