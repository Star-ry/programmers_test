# 선분 3개가 평행하게 놓여 있습니다. 
# 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 
# lines가 매개변수로 주어질 때, 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 
# solution 함수를 완성해보세요.

import numpy as np

def my_solution(lines):
    answer = 0
    arr = np.array(lines)
    min = np.min(arr[:,0])
    max = np.max(arr[:,1])
    axis = np.zeros(max-min)
    for line in lines:
        temp = line-min
        axis[temp[0]:temp[1]] +=1
    answer = len(np.where(axis>1)[0])
    
    return answer



def solution(lines):
    s1 = set(i for i in range(lines[0][0], lines[0][1]))
    s2 = set(i for i in range(lines[1][0], lines[1][1]))
    s3 = set(i for i in range(lines[2][0], lines[2][1]))
    return len((s1 & s2) | (s2 & s3) | (s1 & s3))


if __name__ == "__main__":
    input = [[0, 5], [3, 9], [1, 10]]
    answer = solution(input)
    print(answer)