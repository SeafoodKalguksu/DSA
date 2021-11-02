'''
if the parentheses are like ‘(())’, the program
returns YES.
The program return NO if the parentheses are like ‘
(()))’ or ‘(()()(’.
'''

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring

def check_paren(parentheses: str):
    '''
    0. return YES if the length of the parentheses is 0 or "()".
    1. find an adjacent rounded brakets like '()' in the parentheses.
    2. remove them in the parentheses.
    3. go to step #0
    𝐎(n²)
    '''
    length: int = len(parentheses)

    if length <= 1:
        return "Yes" if length == 0 else "No"
    elif parentheses == "()":
        return "Yes"
    else:
        for i in range(length - 1):
            if parentheses[i] == '(' and parentheses[i+1] == ')':
                # remove parentheses[i] and parentheses[i+1]
                new_parentheses: str = parentheses[:i] + parentheses[i+2:]
                return check_paren(new_parentheses)

    return "No"


def main():
    '''
    find '()'
    ((())()))) -> No
    (())((())) -> Yes
    '''
    parentheses = input()
    print(check_paren(str(parentheses)))


if __name__ == "__main__":
    main()
