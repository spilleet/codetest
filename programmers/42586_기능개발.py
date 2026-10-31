def solution(progresses, speeds):
    answer = []
    days = []
    for progress,speed in zip(progresses,speeds):
        day = (100-progress+speed-1)//speed
        days.append(day)
    deploy_day=days[0]
    count=1
    for day in days[1:]:
        if day<=deploy_day:
            count+=1
        else:
            answer.append(count)
            deploy_day=day
            count = 1
    answer.append(count)
    return answer
