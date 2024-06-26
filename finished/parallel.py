# 점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.
# [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
# 주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 
# 없으면 0을 return 하도록 solution 함수를 완성해보세요.

def get_incline(x,y):
    try:
        incline = (y[1]-x[1])/(y[0]-x[0])
        return incline
        
    except:
        return float('inf')


def solution(dots):
    answer = 0
    
    for i in range(1,4):
        dots[0], dots[i] = dots[i], dots[0]
        x1, y1, x2, y2 = dots
        if get_incline(x1,y1) == get_incline(x2,y2):
            answer = 1
        if x1 == x2 & y1 == y2:
            answer = 0
    return answer


if __name__ == "__main__":
    dots = [[3, 5], [4, 1], [2, 4], [5, 10]]
    answer = solution(dots)
    print(answer)