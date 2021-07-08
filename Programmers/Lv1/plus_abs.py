# 음양 더하기
def solution(absolutes, signs):
    if len(absolutes) != len(signs):
        raise ValueError

    answer = 0
    for num, sign in zip(absolutes, signs):
        if not sign:
            answer += num * -1
        else:
            answer += num

    # another solution
    # answer = sum([num if sign else -1*num for num, sign in zip(absolutes, signs)])

    return answer
