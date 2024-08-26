from collections import defaultdict
def solution(n, m, name):
    name_dict = defaultdict(int)
    dls_people = list()
    for x in name:
        name_dict[x] += 1
        if name_dict[x] == 2:
            dls_people.append(x)
    print(len(dls_people))
    for x in sorted(dls_people):
        print(x)

arr = []
n, m = map(int, input().split())

for i in range(n+m):
    arr.append(input())

solution(n, m, arr)