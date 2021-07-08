# 두 개 뽑아서 더하기
def solution(numbers):
    answer = []
    for front_idx, num_front in enumerate(numbers):
        for back_idx, num_back in enumerate(numbers):
            if front_idx == back_idx:
                continue
            tmp = num_front + num_back
            answer.append(tmp)

    # another solution(best)
    # for front_idx, num in enumerate(numbers):
    #     for back_idx in range(front_idx+1, len(numbers)):
    #         answer.append(num + numbers[back_idx])

    return sorted(list(set(answer)))
