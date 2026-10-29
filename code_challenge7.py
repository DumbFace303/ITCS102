grd = int(input("Input size > "))

cen = grd//2

if cen % 2 == 0 :
    grd += 1





for a in range(grd) :
    for b in range(grd):
        d = abs(a- cen) + abs (b - cen)
        if d <= cen and d % 2 == cen % 2 :
            print("*",end=" ")
        else :
            print(" ",end=" ")

    print()