# 머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 
# 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 
# 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.


import re


def my_solution(babbling):
    answer = 0
    keys = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        check = True
        while (bab != []) & (check == True):
            check = False
            for key in keys:
                idx = bab.find(key)
                if idx == 0:
                    bab = bab[len(key):]
                    check = True
                else:
                    continue
        if bab == '':
            answer += 1
    return answer


# 최대한번은 적용이 안되지 않나?
def solution(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    cnt=0
    for e in babbling:
        if regex.match(e):
            cnt+=1
    return cnt



if __name__ =="__main__":
    babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
    answer = solution(babbling)
    print(answer)