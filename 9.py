# lambda functions


def add(x,y):
    return x+y
add(5,3)
# can also be writen as
add = lambda x,y :x+y
add (5,3)
# OR 
(lambda x,y:x+y)(5,3)

def make_adder(n):
    return lambda x:x+n
p3=make_adder(3)
p5=make_adder(5)
p3(4)    # O/P: 7
p5(4)    # O/P: 9


