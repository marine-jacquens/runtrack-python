def draw_triangle(height):

    leftLine = '/'
    rightLine = "\\"
    horizontalLine = '_'

    a = 10
    c = 0
    while a > height:
        
        space  = ' '
        rightSide = (space*c) + rightLine
        c+=2

        a-=1
        leftSide = (space*a) + leftLine 

        if a == height:
            print(leftSide+horizontalLine*8+rightLine)
        else:
            print(leftSide+rightSide)

    
draw_triangle(5)