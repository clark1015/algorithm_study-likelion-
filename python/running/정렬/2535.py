number_of_students = int(input())
student_information_list = []
winner_frequency_of_country = {} 
winner_result_list = []
#학생들의 정보를 수집하고 점수를 기준으로 정렬한다
for i in range(number_of_students):
    country, std, score = map(int, input().split())
    student_information_list.append((country, std, score))
student_information_list.sort(key=lambda x:x[2])

while student_information_list:
    #우승자 국가 빈도수를 작성한다
    if student_information_list[-1][0] in winner_frequency_of_country.keys():
        winner_frequency_of_country[student_information_list[-1][0]] += 1
    else:
        winner_frequency_of_country[student_information_list[-1][0]] = 1
    #빈도수가 2보다 크면 수상 명부에 작성하지 않는다. 그게 아니라면 수상자 명부에 작성
    if winner_frequency_of_country[student_information_list[-1][0]] >= 3:
        del student_information_list[-1]
    else:
        winner_result_list.append(student_information_list[-1])
        del student_information_list[-1]
    
    if len(winner_result_list) > 3:
        break

for i in range(3):
    print(winner_result_list[i][0], winner_result_list[i][1])



