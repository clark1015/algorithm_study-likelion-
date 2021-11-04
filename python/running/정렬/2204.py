while True:
    word_list = []
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        word = input()
        word_list.append((word, word.lower()))
    word_list.sort(key=lambda x : x[1])
    print(word_list[0][0])