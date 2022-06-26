def mutiply(x,y):
    if x == 1:
        return y
    else:
        return y + mutiply(x-1, y)



def main():
    x = int(input('Enter x :'))
    y = int(input('Enter y :'))

    print(mutiply(x,y))

main()