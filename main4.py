def index_power(array, n):
    if(n>=len(array)):
        return -1
    else:
        return array[n]**n
print(index_power([1, 2], -1))