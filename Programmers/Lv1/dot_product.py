# 내적
def solution(a, b):
    answer = 0
    for a_num, b_num in zip(a, b):
        answer += a_num * b_num

    # another solution
    # answer = sum(map(lambda i: a[i] * b[i], range(len(a))))

    return answer
