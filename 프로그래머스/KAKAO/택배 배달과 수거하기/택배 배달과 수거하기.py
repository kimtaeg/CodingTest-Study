def solution(cap, n, deliveries, pickups):
    answer = 0
    # 배달이 남은 가장 먼 집의 인덱스
    d = n - 1 
    # 수거가 남은 가장 먼 집의 인덱스
    p = n - 1  

    while (True):
        # 할 일이 없는 집은 건너뛰기
        while (d >= 0 and deliveries[d] == 0):
            d -= 1
        while (p >= 0 and pickups[p] == 0):
            p -= 1

        # 배달 수거 모두 끝났으면 종료
        if (d < 0 and p < 0):
            break

        # 거리 구하기 
        answer += (max(d, p) + 1) * 2

        # 먼 집부터 cap만큼 배달
        box = cap
        while d >= 0 and box > 0:
            take = min(deliveries[d], box)
            deliveries[d] -= take
            box -= take
            if deliveries[d] == 0:
                d -= 1

        # 먼 집부터 cap만큼 수거
        box = cap
        while p >= 0 and box > 0:
            take = min(pickups[p], box)
            pickups[p] -= take
            box -= take
            if pickups[p] == 0:
                p -= 1

    return answer