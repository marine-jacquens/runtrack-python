thislist = [10,82,83,78,43]

def gradeEvaluation(arg):

    x = 0
    
    while x < len(thislist):
        if thislist[x] > 40:
            a = 0
            while a < 100:
                a+=1
                if a % 5 == 0:
                    b = 0
                    while b < 2:
                        b+=1
                        if thislist[x] == a - b:
                            thislist[x] = a

        x+=1


gradeEvaluation(thislist)
print(thislist)