## test 4 decorator
import math 
def count_calls(function): 
    def wrapper(*args, **kwargs):
        for i, value in enumerate(args, start=1):
            print(f"{function.__name__} call #{i}")
            result = function(*args, **kwargs)
            return result
    return wrapper
    
@count_calls #add = count(add) 
def add(*args):
    return sum(args)

print(add(2, 3, 4, 5))

@count_calls #multiply = count_calls(multiply) 
def multiply(*args): 
    return math.prod(args)
print(multiply(3,3,3))