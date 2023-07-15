1. Strings are immutable sequences so chars:
    a. left-to-right  positional order
    b. cannot be changed in-place

2. In Python 3.0 there are three string types: 
    str is used for Unicode text (ASCII or otherwise),
    bytes is used for binary data (including encoded text),
    bytearray is a mutable variant of bytes

3. Single ' and Double-Quoted " Strings Are the Same

4. Python automatically concatenates adjacent string literals in any expression:
>>> title = "Meaning " 'of' " Life"
>>> title
'Meaning of Life'

Adding commas between these strings would result in a tuple, not a string:
>>> title = 'Meaning', "of", 'life'
>>> title
('Meaning', 'of', 'life')

5. \n - new line, \t - tab

The interactive echo (>>>) shows the special characters as
escapes, but print interprets them instead:
>>> s
'a\nb\tc'
>>> print(s)
a
b   c
>>> len(s)
5           # The two characters \n stand for a single character —the byte containing the binary value
              of the newline character. same for \t

6. To code literal backslashes explicitly such that they are retained in your strings, 
double them up (\\ is an escape for one \) or use raw strings 

7. IMPORTANT! 
Use r (raw string) before opening quote to turn off '\' escape mechanism:

>>> path = 'C:\new\text.dat'
>>> path
>>> print(path)
C:
ew      ext.dat

but 

>>> path = r'C:\new\text.dat'
>>> path
'C:\\new\\text.dat'             # as python code
>>> print(path)
C:\new\text.dat                 # user friendly format
