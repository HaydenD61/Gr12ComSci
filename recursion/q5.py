def f(array):
    if len(array) == 0:
        return None
    elif len(array) == 1:  
        return array[0]
    else:
        return max(array[0], f(array[1:]))
array = [2, 45, 67, 12, 3]
print(f(array))