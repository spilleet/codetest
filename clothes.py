def solution(clothes):
    answer = 0
    cloth_dict = {}
    for cloth in clothes:
        if cloth[1] not in cloth_dict:
            cloth_dict[cloth[1]] = 0
        cloth_dict[cloth[1]]+=1
    val_list = list(cloth_dict.values())
    new_val = [x+1 for x in val_list]
    temp = 1
    for a in new_val:
        temp*=a
    answer = temp-1
    return answer