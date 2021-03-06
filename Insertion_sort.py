import random

def insertion_sort(list):
    n = len(list)

    for i in range(n - 1):  # List is considered sorted at the beginning
        value = list[i + 1]
        # print(f"---------------\t{value}")
        # print(list)
        for j in range(i + 1):  # Comparing with all the values in the left
            # print("sorting")
            if value < list[i - j]:
                list[i - j], list[i - j + 1] = list[i - j + 1], list[i - j]
    return list


if __name__ == '__main__':
    list_size = int(input("Enter the size of the list: "))
    
    list = [random.randint(1, 100) for i in range(list_size)]
    print(list)

    sorted_list = insertion_sort(list)
    print(sorted_list)