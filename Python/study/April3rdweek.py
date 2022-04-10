# def solution(price, money, count):
#     cost = ((1 * price) + (count * price)) * (count // 2)
#     # count 홀수인 경우
#     if count % 2 != 0:
#         cost += ((count // 2) + 1) * price
#     answer = 0    
#     if cost > money:
#         answer = cost - money
#     return answer

# # 놀이기구의 이용료는 price - 놀이기구를 n번째 이용한다면 이용료의 N배를 받기로
# # 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마나 모자른지를 return
# # 시간 복잡도를 N(1)로 만들기 위해서 위와 같은 로직을 작성


# def solution(sizes):
#     row, col = 0, 0
# #     명함의 가로, 세로 중 큰 값을 가로로 작은 값을 세로로 두어 가로 중에 큰 값, 세로 중에 큰 값으로 계산
#     for size in sizes:
#         a, b = size
#         if a < b:
#             row = max(b, row)
#             col = max(a, col)
#         else:
#             row = max(a, row)
#             col = max(b, col)
#     answer = row * col
#     return answer

# # 가로 세로 명함들의 사이즈 중에 가장 큰 명함에 맞춰서 지갑을 제작
# # 가로 세로의 길이를 서로 바꿀 수 있도록 함

# # 결과를 저장하는 변수
# result = 0
# # dfs
# def dfs(k, dungeons, visited, count):
#     global result
# #    dungeons에서 탐색하지 않는 부분을 탐색
#     for i in range(len(dungeons)):
#         if not visited[i] and k >= dungeons[i][0]:
#             visited[i] = True
#             dfs(k - dungeons[i][1], dungeons, visited, count + 1)
#             visited[i] = False
#     print(visited)
#     result = max(result, count)

# def solution(k, dungeons):
#     global result
#     visited = [False] * len(dungeons)
#     count = 0
#     dfs(k, dungeons, visited, count)
#     return result

# # 던전을 탐험하기 필요한 최소 필요 피로도와 던전 탐험을 마쳤을 때 소모되는 소모 피로도
# # 던전을 최대한 많이 탐험하려고 한다.

INF = int(1e15)

def solution(line):
    answer = []
#     좌표값을 저장하는 리스트
    spots = []
#     별찍기를 위한 가로, 세로 길이
    min_x, max_x, min_y, max_y = INF, -INF, INF, -INF
    for i in range(len(line)):
        a, b, e = line[i]
        for j in range(i + 1, len(line)):
            c, d, f = line[j]
            if ( a * d ) - ( b * c ) != 0:
                x = (( b * f ) - ( e * d )) / (( a * d ) - ( b * c ))
                y = (( e * c ) - ( a * f )) / (( a * d ) - ( b * c ))
                if x - int(x) == 0 and y - int(y) == 0:
                    min_x = min(min_x, int(x))
                    max_x = max(max_x, int(x))
                    min_y = min(min_y, int(y))
                    max_y = max(max_y, int(y))
                    spots.append((int(x), (int(y))))
#   별찍기 - O(r * c)
    for j in range(max_y, min_y - 1, -1):
        temp = ""
        for i in range(min_x, max_x + 1):
            if (i, j) in spots:
                temp += '*'
            else:
                temp += '.'
        answer.append(temp)
    return answer

# line으로 주어진 선들을 그려서 선들이 곂쳐지는 점들을 표현
# 교점에 대한 계산을 각각으로 실행