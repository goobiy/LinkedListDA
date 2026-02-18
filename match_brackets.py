# Choose the one most appropriate of the following ADT for your implementation.
from stack import Stack
from queue import Queue
from deque import Deque
from dll import DLList
from sll import SLList

def match_brackets(s: str) -> bool:
    """
    Returns True if the sting has matching brackets, otherwise False.
    The program checks if for each bracket ( '(', '[' '}' ) there is a matching
    closing bracket. Note, the order and type of the brackets is important.
    For example, if you open a '(' and then a '[', then you need to "close" first
    the ']' before the ')'.
    An example of a matching bracket sting is for example
        "(a [b (c {dd} ) ] [2] )"
    where the following strings are not:
        "(a [b ) ]"  <--- closes [ with a )
        "]b ["   <--- close with ] before opening
        "{{ a }"   <-- missing }
    """

    my_list = SLList()
    stack = Stack(my_list)

    for i in s:
        if stack.is_empty() and i in ")]}":
            return False
        if i in "([{":
            stack.push(i)
        else:
            if i == ")":
                if "(" == stack.top():
                    stack.pop()
                    continue
                else:
                    return False    # a mismatch like [)
            elif i == "]":
                if "[" == stack.top():
                    stack.pop()
                    continue
                else:
                    return False
            elif i == "}":
                if "{" == stack.top():
                    stack.pop()
                    continue
                else:
                    return False

    return stack.is_empty()

def main():
    name = 'brackets.txt'
    try:
        with open(name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                print(f'{line:40} {match_brackets(line)}')
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()