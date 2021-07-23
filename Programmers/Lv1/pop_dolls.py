# 2019 카카오 개발자 겨울 인턴십 : 크레인 인형뽑기 게임
def solution(board, moves):
    answer = 0

    pre_dolls = ['']
    line_dict = {idx: 0 for idx in range(1, len(board)+1)}
    for mov in moves:
        which_line = line_dict[mov]
        if which_line > len(board) - 1:
            continue

        mov -= 1
        while board[which_line][mov] == 0:
            which_line += 1
        append_doll = board[which_line][mov]

        if pre_dolls[-1] == append_doll:
            pre_dolls.pop()
            answer += 2
        else:
            pre_dolls.append(append_doll)
        line_dict[mov+1] = which_line + 1

    return answer
