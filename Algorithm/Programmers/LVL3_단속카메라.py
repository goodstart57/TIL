"""프로그래머스 Level3 단속카메라

routes에는 차량별 진입, 진출 지점이 기입되어 있다.

단속카메라를 최소 개수로 설치했을때 갯수를 구해라.
"""


def solution(routes):
    answer = 0
    camera = -30001
    
    routes = sorted(routes, key=lambda x: x[1])
    
    for route in routes:
        if camera < route[0]:
            camera = route[1]
            answer += 1
    
    return answer