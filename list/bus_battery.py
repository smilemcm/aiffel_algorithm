import sys
from collections import deque


sys.stdin = open("bus_battery.txt","rt")
T = int(input())

for t in range(T):
    k, n, m = map(int, input().split())
    battery_charger_list = list(map(int, input().split()))


    bus_stations = [0] * (n)
    battery = k
    battery_refill_cnt = 0

    #### 모든 정거장에 충전소가 있던 없던 일단 0으로 세팅
    for i in range(len(bus_stations)):
        if i in battery_charger_list:
            bus_stations[i] = 1


    ### 여기서 부터는 실제 시뮬레이션
    for i in range(1,len(bus_stations)):
        battery = battery - 1


        ## 경우할 정류소에 배터리 충전소가 있을경우
        if (sum(bus_stations[i+1 : i+1+battery])>0) or (n-1==i and battery > 0):
            continue
        ### 이 버스 종류장에 충전소가 있으면 충전
        elif bus_stations[i] == 1:
            battery = k
            battery_refill_cnt = battery_refill_cnt + 1
            continue

        if battery == 0 and bus_stations[i] == 0:
            battery_refill_cnt = 0
            break

    #print(t)
    print(t+1, battery_refill_cnt)



