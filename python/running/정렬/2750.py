#삽입 정렬 풀이
n = int(input())
num_list = []
for i in range(n):
    num = int(input())
    num_list.append(num)

for i in range(1, len(num_list)):
    while i>0 and num_list[i] < num_list[i-1]:
        num_list[i], num_list[i-1] =  num_list[i-1], num_list[i]
        i-=1

for k in num_list:
    print(k)
   

#2nd 풀이
x = int(input())
num_list = []
for i in range(x):
    num_list.append(int(input()))
num_list1 = sorted(num_list)
for i in range(len(num_list)):
    print(num_list1[i])