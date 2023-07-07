Dymanic Type Model in Python

Variable creation

A variable is created when your code first assigns it a value.
Future assignments change the value of the already created variable. Technically,
Python detects some names before your code runs, but you can think of it as though
initial assignments make variables.

Variable types
A variable never has any type information or constraints associated with it. The
notion of type lives with objects, not names. Variables are generic in nature; they
always simply refer to a particular object at a particular point in time.

Variable use
When a variable appears in an expression, it is immediately replaced with the object
that it currently refers to, whatever that may be. Further, all variables must be
explicitly assigned before they can be used; referencing unassigned variables results
in errors.

In sum, variables are created when assigned, can reference any type of object, and must
be assigned before they are referenced. This means that you never need to declare names
used by your script, but you must initialize names before you can update them; coun-
ters, for example, must be initialized to zero before you can add to them

For example, when we say this:

``` a = 3 ```

at least conceptually, Python will perform three distinct steps to carry out the request.
These steps reflect the operation of all assignments in the Python language:
1. Create an object to represent the value 3.
2. Create the variable a, if it does not yet exist.
3. Link the variable a to the new object 3.