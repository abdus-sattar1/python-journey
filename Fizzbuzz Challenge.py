
user_input = int(input("What is your number? "))
n = (user_input) + 1

numbers_list = list(range(1,n))

answer = []

for count in numbers_list:
    if count % 3 == 0 and count % 5 == 0:
        answer.append('FizzBuzz')
    elif count % 3 == 0:
        answer.append('Fizz')
    elif count % 5 == 0:
        answer.append('Buzz')
    else:
        answer.append(count)

print(answer)