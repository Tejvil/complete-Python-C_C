# basic exception handeling

def spam (divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError as e :
        print (f'Error"+: Invalid arg : {e}')
    finally:
        print("__division finished__")

print (spam(2))
print (spam(12))
print (spam(0))
print (spam(1))
