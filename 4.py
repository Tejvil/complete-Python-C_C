import random
import sys

for i in range(5):
    print (random.randint(1,10))

while True:
    print ('type exit to exit.')
    response = input()
    if response == 'exit': 
        sys.exit()
    print (f"you typed {response}")
    

