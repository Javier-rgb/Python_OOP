import random

def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        print(left, "-" * 5, right)

        # Recursive Loops
        merge_sort(left)
        merge_sort(right)

        # Iterators
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            print(left, "-" * 5, right)
            if left[i] < right[j]:
                list[k] = left[i]
                i = i + 1
            else:
                list[k] = right[j]
                j = j + 1
            
            k = k + 1
        
        while i < len(left):
            list[k] = left[i]
            i = i + 1
            k = k + 1
        
        while j < len(right):
            list[k] = right[j]
            j = j + 1
            k = k + 1
        
        print(f'LEFT: {left}, RIGHT {right}')
        print(list)
        print('-' * 50)

    return list



if __name__ == '__main__':
    list_size = int(input("Enter the size of the list: "))
    
    list = [random.randint(1, 100) for i in range(list_size)]
    print(list)

    sorted_list = merge_sort(list)
    print(sorted_list)