# list 

spam = ['cat', 'bat', 'dog', 'rat']

spam[0:4]
spam[0:-1]
spam2 = spam[:]    #creats a copy of the list.
spam.append('pig')   #does not apend in the copy .i.e spam2
spam
spam2
len(spam)
spam[1]='elephant'
spam
spam[2] = spam[1]
spam
del spam[2]


([1,2,3,4] + ['a','b','c'])
['X', 'Y', 'Z'] * 3

spam = [1,2,3]
spam = spam + ['A','B','C']
spam

# for in list
supplies = ['pens','staplers', 'flame-throwers', 'blinders']
# for i, supply in enumerate(supplies):             # using enumerate makes i the index and supply is the each items in the list 
    #  print (f'Index {i} in supplies is : {supply}')

    
# zip - loop through multiple list using zip()
name = ['Pete', 'John', 'Alice', 'Bob']
age = [6,23,44,11]
# for n,a in zip (name,age):
#     print(f'{n} is {a} years old')


# .get
picnic_items = {'apples': 5, 'soups': 2}
(f"I am bringing {picnic_items.get('soups', 0)} soups.")
(f"I am bringing {picnic_items.get('eggs', 0)} eggs.")

# merge 2 dictionaries
x = {'a':1 , 'b':2}
y = {'z':9,'b':5}
z = {**x , **y}
(z)


# creating sets : used to remove/eleminate duplicate entries
s={1,2,3}
s= set([1,2,3])
s={1,2,3,2,4,3}
(s)
s.add(6)
s.update([2,3,4,5,6,7])
s.remove(3)
s.discard(7)
(s)
s1 = {1,2,3}
s2 = {3,4,5}
(s1.union(s2))
s3 = {2,3,4}
(s1.intersection(s2, s3))
(s1.difference(s2))
(s2.difference(s1))


# list comprehensions
a = [1,3,5,7,9,11]
[i - 1 for i in a]

# set comprehensions
b = {'abc','def'}
{s.upper() for s in b}

# dict comprehensions
c = {'name':'Pooka', 'age':5}
{v: k for v in c.items()}

