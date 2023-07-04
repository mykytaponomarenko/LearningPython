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