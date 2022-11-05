def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print('Largest number ', largestItem(numbers, 0, len(numbers)-1))


def largestItem(list, start, end):
    if start > end:
        return 0
    else:
        print(list[start])
        largestItem(list, start+1, end)


main()
