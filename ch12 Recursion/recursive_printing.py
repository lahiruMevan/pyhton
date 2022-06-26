def printNum(num):
    if num == 1:
        print(num)
    else: 
        
        printNum(num - 1)
        print(num)

def main():
    num  = int(input('Enter number count: '))
    printNum(num)


main()