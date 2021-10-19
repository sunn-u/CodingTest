# 프로그래머스 Lv.2 : H-INDEX(https://programmers.co.kr/learn/courses/30/lessons/42747)
# 2021-10-19 : sort 를 사용하지 않고 풀려고 함
def solution(citations):
    max_count = len(citations)
    count_dict = {n: 0 for n in range(0, max_count + 1)}

    for cit in citations:
        if cit >= max_count:
            count_dict[max_count] += 1
        else:
            count_dict[cit] += 1

    inyong = 0
    for n in range(max_count, 0, -1):
        inyong += count_dict[n]
        if inyong >= n:
            return n
    return 0

# 다른 사람 풀이 1.
def other_solution_1(citations):
    # 오름차순으로 정렬
    citations = sorted(citations)
    l = len(citations)

    # l-i 는 제일 뒤의 인덱스부터 내려오는 격이자 남아있는 논문의 수로 이해
    # 예를 들어 i=0 일 때, l-i 는 전체 논문의 수가 된다.
    # 이때 인용된 횟수가 제일 적은 citations[0] 이 전체 논문의 수를 넘는다면
    # l-i 를 그대로 return 하는 식
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0


# 다른 사람 풀이 2.
def other_solution_2(citations):
    # 내림차순으로 정렬
    citations.sort(reverse=True)

    # 논문의 인용횟수를 내림차순으로 정렬한 다음에
    # 첫번째 값부터 들여다보는 코드의 의미
    # = h 번째 논문까지는 h 번 이상 인용이 되었다.

    # [10000, 98, 88, 2, 1] 인 경우,
    # idx=3 까지는 10000번 인용된 논문, 98 번 인용된 논문, 88번 인용된 논문
    # 모두 3번 이상 인용이 되었으므로 h_index=3
    # 그러나 idx=4 에서는 2번 밖에 인용이 안 되었기에
    # h_index=4 조건인 4 번째 논문까지 4 번 이상 인용이 되었다를 만족시키기 못함
    # 여기서는 map 함수를 사용하느라 max(map) 을 해줬지만
    # 최대값을 구하는 문제이기에 중간에 for + return 을 해줘도 될듯
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
