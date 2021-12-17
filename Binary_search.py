import random

def binary_search(list, start, end, value, i):
    if start > end:
        return False
    
    mid = (start + end) // 2

    if list[mid] == value:
        print(f"Number of tries: {i}")
        return True
    elif list[mid] < value:
        return binary_search(list, mid + 1, end, value, i + 1)
    elif list[mid] > value:
        return binary_search(list, start, mid - 1, value, i + 1)

if __name__ == '__main__':
    list_size = int(input("Enter the size of the list: "))
    value = int(input("Enter the value you want to check: "))

    list = sorted([random.randint(1, 100) for i in range(list_size - 1)])
    print(list)

    found = binary_search(list, 0, len(list), value, 1)

    print(f'The element {value} {"was found" if found else "was not found"} in the list')