def solution(phone_book):
    answer = True
    phone_hash=set(phone_book)
    for numbers in phone_hash:
        for i in range(1,len(numbers)):
            temp = numbers[:i]
            if temp in phone_hash:
                return False
    return answer