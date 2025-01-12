factor_3 = 3
factor_5 = 5

for count in range(1, 10001):
        if count % factor_3 == 0 or factor_5 == 0:
            print('fizzbuzz')
        else:
            print(count)