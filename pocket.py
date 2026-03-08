def solution(nums):
    answer = 0
    pocket_dict = {}
    for numb in nums:
        if numb not in pocket_dict:
            pocket_dict[numb] = 0
        pocket_dict[numb]+=1
    count = len(pocket_dict)
    if count >=len(nums)//2:
        answer = len(nums)//2
    else:
        answer = count
    return answer
        