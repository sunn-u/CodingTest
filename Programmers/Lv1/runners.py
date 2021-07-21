# 완주하지 못한 선수
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p
        return participant[-1]

    # another solution - 1. use collections.Counter
    # import collections
    # answer = collections.Counter(participant) - collections.Counter(completion)
    # return list(answer)[0]

    # another solution - 2. use hash
    # temp = 0
    # dic = {}
    # for part in participant:
    #     dic[hash(part)] = part
    #     temp += int(hash(part))
    # for com in completion:
    #     temp -= hash(com)
    #
    # return dic[temp]
