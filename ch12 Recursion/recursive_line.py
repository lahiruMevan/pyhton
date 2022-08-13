def recLine(n):
    if n == 1:
        printStar(n)
    else:
        printStar(n)
        print()
        recLine(n-1)


def printStar(num):
    if(num == 1):
        print('*', end="")
    else:
        print('*', end="")
        printStar(num-1)


def main():
    num = int(input('Input a number to print * :'))
    recLine(num)


main()
