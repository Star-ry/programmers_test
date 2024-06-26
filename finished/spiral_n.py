# 양의 정수 n이 매개변수로 주어집니다. 
# n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 
# 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.

import numpy as np

def solution(n):
    guide = [[0,1],[1,0],[0,-1],[-1,0]]
    arr = np.zeros((n,n)).astype(int)
    
    rot_cnt = 0
    axis = np.array([0,0])
    for i in range(1,n*n+1):
        arr[axis[0], axis[1]] = int(i)
        try :
            temp_axis = axis + guide[rot_cnt%4]
            if arr[temp_axis[0], temp_axis[1]] != 0:
                rot_cnt += 1
        except:
            rot_cnt += 1
        axis += guide[rot_cnt%4]
    answer = arr.tolist()
    return answer


if __name__ == "__main__":
    input = 4
    answer = solution(input)
    print(answer)