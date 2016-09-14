from timeit import timeit
test_cases  = int(input())
for i in range(test_cases):
    multiples = []
    sum_add = 0
    number = int(input())
    for i in range(0, number):
        if i%3==0 or i%5==0:
            sum_add += i
    print(sum_add)
