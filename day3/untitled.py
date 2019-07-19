def numbers(mylist):
    list_of_numbers = []
    for el in mylist:
        try:
            list_of_numbers.append(int(el))
        except ValueError:
            pass
    return list_of_numbers

if __name__ == '__main__':
    l = ["sync", "c", "33", "44"]
    print(numbers(l))
