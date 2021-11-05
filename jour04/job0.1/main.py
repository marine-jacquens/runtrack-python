def program(number):

    return 1 if (number==1 or number==0) else number * program(number-1)

number = int(input('Entrez un nombre '))
program(number)
print("La factorielle de",number,"est",program(number))
