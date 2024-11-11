#This function returns results following these basic operations

def basic_operations(a, b):
    return{
        'Addition': a+b,
        'Subtraction': a-b,
        'Multiplication': a*b,
        'Division': a/b if b!=0 else 'undefined'
        }

#Output
print(basic_operations(100, 4))