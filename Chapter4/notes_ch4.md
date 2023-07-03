1. Core data types

Object type     Example literals/creation
-------------------------------------
Numbers         1234, 3.1415, 3+4j, Decimal, Fraction       Immutable
Strings         'spam', "guido's", b'a\x01c'                Immutable       Seqeunce
Lists           [1, [2, 'three'], 4]                        Mutable         Seqeunce
Dictionaries    {'food': 'spam', 'taste': 'yum'}            Mutable
Tuples          (1, 'spam', 4, 'U')                         Immutable       Seqeunce
Files           myfile = open('eggs', 'r')
Sets            set('abc'), {'a', 'b', 'c'}
Booleans        True, False, 1, 0

Program unit types                  Functions, modules, classes
Implementation-related types        Compiled code, stack tracebacks 

2. Special characters represented as backslash escape sequences

\n - newline
\t - tab
\0 - binary zero byte which does not terminate string. See print('A\0B\0C) and it's len()

print(ord('\n')) will result in 10 as \n is a byte with the binary value 10 in ASCII


3. Regular Expressions
    3.1 import re
    3.2 'r' at the start of a string literal, also known as a raw string literal, denotes a raw string (no escape interpretations) 

>>> import re
>>> pattern = r'Hello[ \t]*(.*)world'
>>> text = 'Hello      Python world'
>>> match = re.match(pattern, text)
>>> match.group(1)


This example searches for a substring that begins with the word “Hello,” followed by
zero or more tabs or spaces, followed by arbitrary characters to be saved as a matched
group, terminated by the word “world.” If such a substring is found, portions of the
substring matched by parts of the pattern enclosed in parentheses are available as groups

>>> match = re.match('/(.*)/(.*)/(.*)', '/usr/home/docs')
>>> match.groups()