i = 0 

# while i < 100:
#     print(i)
#     i +=1

while i < 100:
    i +=1
    if i % 3 == 0 and i % 5 == 0:   
        print('FizzBuzz')
        continue
    elif i % 5 == 0:
        print('Buzz')
        continue
    elif i % 3 == 0:
        print('Fizz')
        continue
    else: 
        print(i)
       