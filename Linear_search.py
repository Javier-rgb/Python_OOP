import random

def linear_search(list, value):
    found = False
    i = 1

    for element in list:    # O(n)
        if element == value:
            found = True
            break
        else:
            i = i + 1
    
    print(f"Number of tries: {i}")
    return found


if __name__ == '__main__':
    list_size = int(input("Enter the size of the list: "))
    value = int(input("Enter the value you want to check: "))

    list = [random.randint(1, 100) for i in range(list_size - 1)]

    print(list)
    found = linear_search(list, value)

    print(f'The element {value} {"was found" if found else "was not found"} in the list')
