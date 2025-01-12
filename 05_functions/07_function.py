# function with *args
#write a function that takes a variable number of arguments and returns their sum

def summ_all(*args):
    print(args)
    return sum(args)

print(summ_all(1, 2))
print(summ_all(1, 2, 3, 4, 5))
print(summ_all(1, 2, 3, 4, 5, 6, 7, 8))