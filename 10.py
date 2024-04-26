# args and kw-args 


# *args 
def fruits (*args):
    for fruit in args:
        print(fruit)
fruits("apples", "banana", "grapes")

# **kwargs -keyword args

def fruit(**kwargs):
    for key, value in kwargs.items():
        print("{0}:{1}".format(key, value))
fruit(name = "apple", color = "red")

# *args and **kwargs
def myFun(*args, **kwargs):
	print("args: ", args)
	print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")
