rectanglePart1 = '|--------|'
rectanglePart2 = '|        |'
 
def draw_rectangle(x,y):

    if x == 10 and y == 3:

        a = 0

        while a < 3:
            a+=1
            if a == 1 or a == 3 :
                print(rectanglePart1)
                continue
            else:
                print(rectanglePart2)    
        
draw_rectangle(10,3)