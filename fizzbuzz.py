def fizzbuzz():
    for n in range(1,101):
        if n%15==0:
            print('fizzbuzz')
        elif n%3==0:
            print('fizz')
        else:
            print(n)
fizzbuzz()
