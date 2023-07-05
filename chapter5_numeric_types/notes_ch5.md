Python Numeric Toolbox

• Integers and floating-point numbers
• Complex numbers
• Fixed-precision decimal numbers
• Rational fraction numbers
• Sets
• Booleans
• Unlimited integer precision
• A variety of numeric built-ins and modules


Basic numeric Literals

Literal                                 Interpretation
1234, −24, 0, 99999999999999            Integers (unlimited size)
1.23, 1., 3.14e-10, 4E210, 4.0e+210     Floating-point numbers
0177, 0x9ff, 0b101010                   Octal, hex, and binary literals in 2.6    
0o177, 0x9ff, 0b101010                  Octal, hex, and binary literals in 3.0
3+4j, 3.0+4.0j, 3J                      Complex number literals

Table 5-2. Python expression operators and precedence

Operators                                                                       Description
yield x                                                                         Generator function send protocol
lambda args: expression                                                         Anonymous function generation
x if y else z                                                                   Ternary selection (x is evaluated only if y is true)
x or y                                                                          Logical OR (y is evaluated only if x is false)
x and y                                                                         Logical AND (y is evaluated only if x is true)
not x                                                                           Logical negation
x in y, x not in y                                                              Membership (iterables, sets)
x is y, x is not y                                                              Object identity tests
x < y, x <= y, x > y, x >= y                                                    Magnitude comparison, set subset and superset;
x == y, x != y                                                                  Value equality operators
x | y                                                                           Bitwise OR, set union
x ^ y                                                                           Bitwise XOR, set symmetric difference
x & y                                                                           Bitwise AND, set intersection
x << y, x >> y                                                                  Shift x left or right by y bits
x + y                                                                           Addition, concatenation;
x – y                                                                           Subtraction, set difference
x * y                                                                           Multiplication, repetition;
x % y                                                                           Remainder, format;
x / y, x // y                                                                   Division: true and floor
−x, +x                                                                          Negation, identity
˜x                                                                              Bitwise NOT (inversion)
x ** y                                                                          Power (exponentiation)
x[i]                                                                            Indexing (sequence, mapping, others)
x[i:j:k]                                                                        Slicing
x(...)                                                                          Call (function, method, class, other callable)
x.attr                                                                          Attribute reference
(...)                                                                           Tuple, expression, generator expression
[...]                                                                           List, list comprehension
{...}                                                                           Dictionary, set, set and dictionary comprehensions

Mixed operators follow operator precedence

As in most languages, in Python, more complex expressions are coded by stringing
together the operator expressions in Table 5-2. For instance, the sum of two multipli-
cations might be written as a mix of variables and operators:
A * B + C * D
So, how does Python know which operation to perform first? The answer to this ques-
tion lies in operator precedence. In expression with more than one
operator, Python groups its parts according to what are called precedence rules, and
this grouping determines the order in which the expression’s parts are computed.
Table 5-2 is ordered by operator precedence:
• Operators lower in the table have higher precedence, and so bind more tightly in
mixed expressions.
• Operators in the same row in Table 5-2 generally group from left to right when
combined (except for exponentiation, which groups right to left, and comparisons,
which chain left to right).

!!! Python always evaluates expressions in parentheses first
before using their results in the enclosing expressions !!!

Example: (X + Y) * Z. X + Y evaluates first

In 3.0+ nonnumeric mixed-type comparisons are not allowed and raise exceptions

