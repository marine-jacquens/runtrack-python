def draw_rectangle(width,height):

    x = '-'
    y = '|'
    b = ' '

    a = 0
    while a < height:
        a+=1
        if a == 2:
            print(y+(b*width)+y)
            continue
        else:
            print(y+(x*width)+y)
        
draw_rectangle(10,3)