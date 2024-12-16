sum = 0
odd = 0
even = 0
for x in range (1,11):
    num=int(input(f'enter number {x}: '))
    sum += num
    if num % 2 == 0:
        odd += num
    else:
        even += num
print(f'The sum of all numbers given is {sum}')
print(f'The odd of all numbers given is {odd}')
print(f'The even of all numbers given is {even}')