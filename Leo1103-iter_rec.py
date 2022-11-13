'''
Iterative power:
base can be float or integer
exponent need to be an integer than is more than or equal to 0
    if exp is 1
        the function will return base
    else if the exp is 0
        the function will return 1
    else
        base will be saved as baseValue so it can be used to multiply
        the loop will run for value of exp
            base will be multiply with baseValue
        the function will return base that calculated
print the result
'''

def iterativePower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    else:
        baseValue = base
        for i in range (exp - 1):
            base *= baseValue
        return base

print(iterativePower(5,3))

'''
Recursive power:
base can be float or integer
exponent need to be an integer than is more than or equal to 0
    if exp is 1
        the function will return base
    else if the exp is 0
        the function will return 1
    else
        return base time the value that get from the same function that have the same base but -1 exponent
        the function will run multiple times until the exponent is 1
print the result
'''

def recursivePower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    else:
        return base * (recursivePower(base, exp - 1))

print(recursivePower(5,3))