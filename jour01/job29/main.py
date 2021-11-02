triangleSide1 = '      /\ '
triangleSide2 = '     /  \ '
triangleSide3 = '    /    \ '
triangleSide4 = '   /      \ '
triangleSide5 = '  /        \ '
triangleSide6 = ' /__________\ '


def draw_triangle(x):
    a = 0
    while a < 6:
        a+=1

        if a == 1:
            print(triangleSide1)
            continue
        elif a == 2:
            print(triangleSide2)
            continue
        elif a == 3:
            print(triangleSide3)
            continue
        elif a == 4:
            print(triangleSide4)
            continue
        elif a == 5:
            print(triangleSide5)
            continue
        elif a == 6:
            print(triangleSide6)
            continue

draw_triangle(5)