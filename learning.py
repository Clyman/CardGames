#binary search practice on words
arr = ["test", "test1", "apple", "orange", "banana", "kiwi", "pomegrenade", "grape", "pineapple"]
word_arr = sorted(arr)

def binary_search(word_arr, target):
    low = 0 
    high = len(word_arr) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_val = word_arr[mid]
        if mid_val == target:
            return mid
        elif mid_val > target:
            high = mid - 1
        elif mid_val < target:
            low = mid + 1

    return -1 

x = binary_search(word_arr, "banana")
print(x)

#linear search 
def linear_search(word_arr, target):
    for index, value in enumerate(word_arr):
        if value == target:
            return index
    return -1 

a = linear_search(word_arr, "banana")
print(a)