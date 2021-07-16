# 2021-07-16 : 소수 만들기
def solution(nums):
    answer = 0

    for f_idx, f_num in enumerate(nums):
        for s_idx, s_num in enumerate(nums[f_idx+1:]):
            for t_idx, t_num in enumerate(nums[f_idx+s_idx+2:]):
                tmp_sum = f_num + s_num + t_num

                break_point = False
                if tmp_sum % 2 == 0:
                    break_point = True
                else:
                    for num in range(tmp_sum)[3::2]:
                        if tmp_sum % num == 0:
                            break_point = True
                            break

                if not break_point:
                    answer += 1

    # another solution - use combinations + 에라토스테네스의 체
    # from itertools import combinations as cb
    # answer = 0
    # for num_tuple in cb(nums, 3):
    #     cb_sum = sum(num_tuple)
    #
    #     tag = 0
    #     for i in range(2, int(cb_sum**0.5)+1):
    #         if cb_sum % i == 0:
    #             tag += 1
    #     if tag == 0:
    #         answer += 1

    return answer
