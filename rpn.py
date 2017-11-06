#!/usr/bin/env python3
import operator
from datetime import datetime
import sys

ops = {
    '+': operator.add,
    '-': operator.sub,
}

def calculate(myarg):
    stack = list()
    size = 0

    for token in myarg.split():
        if (token == 'q'):
            sys.exit(1)
        
        try:
            stack.append(int(token))
            size = size + 1

        except ValueError:
            if (size == 1):
                print("Too less numbers")
                sys.exit(1)
            
            arg2 = stack.pop()
            arg1 = stack.pop()
            function = ops[token]
            
            result = function(arg1, arg2)

            stack.append(result)
            size = size - 1
            print(result)

        if (size > 2 or size < 1):
             print("Too many numbers")
             sys.exit(1)

    return stack.pop()

def main():
    print(datetime.now())
    
    while True:
        input_text = input("rpn calc> ")
        result = calculate(input_text)

if __name__ == '__main__':
    main()
