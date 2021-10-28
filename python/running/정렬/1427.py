n = int(input())
nums = []
while n != 0:
    nums.append(n%10)
    n //= 10
nums.sort(reverse = True)
for i in nums:
    print(int(i), end='')

#-------------------2nd 풀이------------------------
n = int(input())
 
li = []
for i in str(n):
    li.append(int(i))
# li = list(map(int,str(n))) 으로 변경가능
    
li.sort(reverse=True) # 내림차순
 
for i in li:
    print(i,end='')