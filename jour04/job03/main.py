def program(a,x,n):

    a.append(x) 
    print(a)
    if(n > 0):
        x = x * a[0]
        program(a,x,n-1)
    else:
        print('Résultat : ', x)

a =[]    
n=int(input('Entrez un nombre ')) 
x=10
program(a,x,n)
