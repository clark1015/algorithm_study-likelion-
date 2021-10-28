num_list = list(map(int, input().split()))
for i in range(len(num_list)):
    for j in range(i+1, len(num_list)):
        if num_list[i] > num_list[j]:
           num_list[i], num_list[j] = num_list[j], num_list[i]
for i in num_list:
    print(i, end=' ')

