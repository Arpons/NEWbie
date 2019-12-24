num = int(input("정수를 입력하세요 : "))
def first():
    for i in range(2, num + 1):
        cheak = True
        for j in range(2, i):
            if i % j == 0:
                cheak = False
            break
        if cheak:
            print(i, end=" ")

def second():
    num = int(input("정수를 입력하세요 : "))
    for i in range(1, num + 1):
        count = 0
        for j in range(1, i + 1):
            if i%j == 0:
                count += 1
        if count == 2:
            print(j)
