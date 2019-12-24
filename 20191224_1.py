def gcd():
    num = int(input("정수를 입력해주세요 :"))
    a = []
    for i in range(1, num+1):
        if num % i == 0:
            a.append(i)
    print(a == 2)
gcd()