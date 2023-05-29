import heapq, sys

INF = int(2e9)

v, e = map(int, input('vertex개수와 edge의 개수를 입력하세요: ').split())

start = int(input('시작 vertex위치를 입력하세요: '))

graph = [[] for _ in range (v + 1)] # v + 1 하는 이유는 index 0 무시

distance = [INF] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())

    graph[a].append((b, c)) # 노드 a -> b (비용c)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, v = heapq.heappop(q)
        #이미 처리된 노드 무시
        if distance[v] < dist:
            continue

        for i in graph[v]:
            c = dist + i[1]
            
            if c < distance[i[0]]:
                distance[i[0]] = c
                heapq.heappush(q, (c,i[0]))

dijkstra(start)

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print("{}번 노드까지 최단 거리: {}".format(i, distance[i]))