num_list = list(map(int, input().split()))
result = []
for i in range(3):
    result.append(min(num_list))
    num_list.remove(min(num_list))
for i in result:
    print(i, end = ' ')