
## Data Structures and Algorithms in Python
This repository contains Python implementations of three fundamental functions related to Data Structures and Algorithms.

Question 1: Balanced Parentheses (Stacks)


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
This function determines whether a given expression containing parentheses, curly braces, and square brackets is balanced.

Question 2: Remove Duplicates (Sequences - Lists/Tuples)

def remove_duplicates(sequence):
    seen = set()
    result = []

    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

# Test the function
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]
This function removes duplicates from a sequence (list or tuple) while maintaining the original order of elements.

Question 3: Word Frequency (Dictionaries)

import re

def word_frequency(sentence):
    words = re.findall(r'\b\w+\b', sentence.lower())
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

# Test the function
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)


## AUTHOR
Festus Sulumeti