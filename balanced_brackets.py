def is_balanced(expression):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or opening_brackets.index(stack.pop()) != closing_brackets.index(char):
                return False

    return not stack

# Test the function
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
